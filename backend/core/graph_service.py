import networkx as nx
import json
import os
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta
from backend.agents.schemas import MemoryEntry
from backend.core.enricher import graph_enricher

logger = logging.getLogger("vital_graph")

GRAPH_FILE = "backend/data/knowledge_graph.json"

class GraphService:
    """
    Persistent GraphRAG service using NetworkX.
    Constructs a temporal knowledge graph from memories to detect complex risk patterns.
    """
    def __init__(self):
        self.graph = nx.DiGraph()
        self._load_graph()

    def _save_graph(self):
        """Persists graph to disk."""
        try:
            data = nx.node_link_data(self.graph)
            os.makedirs(os.path.dirname(GRAPH_FILE), exist_ok=True)
            with open(GRAPH_FILE, "w") as f:
                json.dump(data, f)
            logger.info("[GraphService] Graph saved.")
        except Exception as e:
            logger.error(f"[GraphService] Save failed: {e}")

    def _load_graph(self):
        """Loads graph from disk."""
        if os.path.exists(GRAPH_FILE):
            try:
                with open(GRAPH_FILE, "r") as f:
                    data = json.load(f)
                self.graph = nx.node_link_graph(data)
                logger.info(f"[GraphService] Loaded graph: {self.graph.number_of_nodes()} nodes.")
            except Exception as e:
                logger.error(f"[GraphService] Load failed: {e}")
                self.graph = nx.DiGraph()

    async def add_memory_node(self, memory: MemoryEntry):
        """
        Adds a single memory and enriches it.
        This replaces the full rebuild approach for incremental updates.
        """
        # 1. Add Base Memory Node
        node_id = memory.id if memory.id else f"mem_{int(datetime.now().timestamp())}"
        ts = datetime.fromisoformat(memory.timestamp) if memory.timestamp else datetime.now()
        
        self.graph.add_node(
            node_id, 
            type="memory", 
            timestamp=ts.isoformat(),
            statement=memory.statement
        )
        
        # 2. Semantic Enrichment (The "Perception" Step)
        enrichment = await graph_enricher.enrich_memory(memory.statement)
        
        for node in enrichment.get("nodes", []):
            # Add Entity Node
            self.graph.add_node(node["id"], type=node["type"], label=node["label"])
            # Link Memory -> Entity
            self.graph.add_edge(node_id, node["id"], relation="MENTIONS")
            
        for edge in enrichment.get("edges", []):
            # Add Entity -> Entity edges
            self.graph.add_edge(edge["source"], edge["target"], relation=edge["relation"])

        # 3. Temporal Link (Find last memory)
        # Simple heuristic: find last added memory node
        # In a real DB, we'd query. Here we can sort nodes or keep track of 'last_memory_id'
        # For now, let's just save.
        self._save_graph()

    def build_graph(self, memories: List[MemoryEntry]):
        """
        Legacy method. We now prefer incremental add_memory_node.
        But for compatibility, we can keep a simplified version or deprecate.
        """
        pass 

    def detect_grind_pattern(self, threshold_minutes: int = 60) -> Dict[str, Any]:
        """
        Detects 'The Grind' using GraphRAG.
        Traverses recent Memory nodes, checks linked 'Activity' entities, and sums duration.
        """
        # 1. Get all Memory nodes sorted by time
        memories = []
        for n, d in self.graph.nodes(data=True):
            if d.get("type") == "memory":
                try:
                    ts = datetime.fromisoformat(d.get("timestamp"))
                    if ts.tzinfo is not None:
                        ts = ts.replace(tzinfo=None)
                    memories.append((n, ts, d))
                except:
                    pass
        
        if not memories:
            return {"detected": False, "duration": 0, "reason": "No memories found"}
            
        memories.sort(key=lambda x: x[1], reverse=True) # Newest first
        
        current_duration = 0
        involved_nodes = []
        
        # 2. Traverse backwards
        for i in range(len(memories)):
            node_id, ts, data = memories[i]
            
            # Check linked entities for "Sedentary" activities
            is_sedentary = False
            activity_label = "Unknown"
            
            # Find neighbors that are Entities
            for neighbor in self.graph.neighbors(node_id):
                n_data = self.graph.nodes[neighbor]
                if n_data.get("type") == "Activity":
                    label = n_data.get("label", "").lower()
                    # Heuristic for sedentary
                    if any(x in label for x in ["code", "coding", "debug", "write", "meeting", "sit"]):
                        is_sedentary = True
                        activity_label = label
                        break
            
            # Fallback: Check statement text if no entity found (Hybrid approach)
            if not is_sedentary:
                text = data.get("statement", "").lower()
                if any(x in text for x in ["code", "coding", "debug", "write"]):
                    is_sedentary = True
                    activity_label = "coding (inferred)"

            if is_sedentary:
                # Calculate duration from previous memory (or default 15m)
                duration = 15 # Default
                if i < len(memories) - 1:
                    prev_ts = memories[i+1][1]
                    diff = (ts - prev_ts).total_seconds() / 60
                    if diff < 120: # If gap is huge, assume break
                        duration = diff
                
                current_duration += duration
                involved_nodes.append(node_id)
            else:
                # Break in chain
                # If we hit a non-sedentary node (e.g. "Went for a walk"), stop counting
                break
                
        if current_duration > threshold_minutes:
            return {
                "detected": True,
                "duration": int(current_duration),
                "reason": f"GraphRAG: Continuous sedentary activity ({activity_label}) for {int(current_duration)}m.",
                "involved_nodes": involved_nodes
            }
            
        return {"detected": False, "duration": int(current_duration), "reason": "Safe limits", "involved_nodes": []}

    def detect_mixed_media_pattern(self) -> Dict[str, Any]:
        return {"detected": False, "reason": "", "involved_nodes": []}

    def get_recent_activity(self, limit: int = 20) -> List[Dict[str, Any]]:
        """
        Retrieves the most recent memory nodes and their linked entities.
        Calculates duration based on time gaps between memories.
        """
        memories = []
        for n, d in self.graph.nodes(data=True):
            if d.get("type") == "memory":
                try:
                    ts = datetime.fromisoformat(d.get("timestamp"))
                    # Ensure naive for comparison
                    if ts.tzinfo is not None:
                        ts = ts.replace(tzinfo=None)
                    memories.append((n, ts, d))
                except:
                    pass
        
        # Sort newest first
        memories.sort(key=lambda x: x[1], reverse=True)
        recent = memories[:limit]
        
        results = []
        for i in range(len(recent)):
            node_id, ts, data = recent[i]
            
            # Calculate Duration (Time until NEXT memory)
            # Since list is newest-first, the "next" event in time is at i-1 (if i>0)
            # But wait, we want duration OF this event. So we look at the *next* memory in chronological order.
            # In a newest-first list:
            # [Now, 10m ago, 30m ago]
            # Duration of "10m ago" is (Now - 10m ago).
            # So we look at i-1.
            
            duration_str = "Unknown"
            if i > 0:
                next_event_ts = recent[i-1][1]
                diff = (next_event_ts - ts).total_seconds() / 60
                if diff < 180: # If gap < 3 hours, assume continuous
                    duration_str = f"{int(diff)} mins"
                else:
                    duration_str = "End of session"
            else:
                duration_str = "Ongoing"

            # Find linked entities
            entities = []
            for neighbor in self.graph.neighbors(node_id):
                n_data = self.graph.nodes[neighbor]
                if n_data.get("type") != "memory":
                    entities.append(f"{n_data.get('label')} ({n_data.get('type')})")
            
            results.append({
                "timestamp": ts.isoformat(),
                "statement": data.get("statement"),
                "duration": duration_str,
                "entities": entities
            })
            
        return results

# Global Instance
graph_service = GraphService()

