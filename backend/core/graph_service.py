import networkx as nx
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta
from backend.agents.schemas import MemoryEntry
import logging

logger = logging.getLogger("vital_graph")

class GraphService:
    """
    Lightweight GraphRAG service using NetworkX.
    Constructs a temporal knowledge graph from memories to detect complex risk patterns.
    """
    def __init__(self):
        self.graph = nx.DiGraph()

    def build_graph(self, memories: List[MemoryEntry]):
        """
        Rebuilds the graph from a list of recent memories.
        """
        self.graph.clear()
        
        sorted_memories = sorted(memories, key=lambda x: x.timestamp)
        
        for i, mem in enumerate(sorted_memories):
            # 1. Add Memory Node
            # Node ID is the memory ID (or index if ID missing)
            node_id = mem.id if mem.id else f"mem_{i}"
            
            # Parse timestamp
            try:
                ts = datetime.fromisoformat(mem.timestamp)
            except ValueError:
                ts = datetime.now() # Fallback

            self.graph.add_node(
                node_id, 
                type="memory", 
                timestamp=ts,
                statement=mem.statement,
                scene=mem.scene,
                outcome=mem.outcome,
                entities=mem.entities or []
            )
            
            # 2. Add Entity Nodes & Edges
            if mem.entities:
                for entity in mem.entities:
                    entity_id = f"ent_{entity.lower()}"
                    self.graph.add_node(entity_id, type="entity", name=entity)
                    self.graph.add_edge(node_id, entity_id, relation="INVOLVES")
            
            # 3. Add Sequential Edges (Temporal)
            if i > 0:
                prev_mem = sorted_memories[i-1]
                prev_id = prev_mem.id if prev_mem.id else f"mem_{i-1}"
                
                # Calculate time delta
                try:
                    prev_ts = datetime.fromisoformat(prev_mem.timestamp)
                    delta_minutes = (ts - prev_ts).total_seconds() / 60
                except:
                    delta_minutes = 0
                
                self.graph.add_edge(prev_id, node_id, relation="NEXT", delta_minutes=delta_minutes)

        logger.info(f"[GraphService] Built graph with {self.graph.number_of_nodes()} nodes and {self.graph.number_of_edges()} edges.")

    def detect_grind_pattern(self, threshold_minutes: int = 60) -> Dict[str, Any]:
        """
        Detects 'The Grind': Continuous high-intensity work without breaks.
        Returns: { "detected": bool, "duration": int, "reason": str, "involved_nodes": List[str] }
        """
        # 1. Identify Work Nodes
        work_nodes = []
        for node, data in self.graph.nodes(data=True):
            if data.get("type") == "memory":
                # Heuristic: Check for "coding", "work", "debug" in statement or scene
                text = (data.get("statement", "") + " " + data.get("scene", "")).lower()
                # Use regex for robust matching
                import re
                work_pattern = r"code|coding|debug|work|writing|implement|refactor|deploy|commit"
                if re.search(work_pattern, text):
                    work_nodes.append((node, data["timestamp"]))
        
        if not work_nodes:
            return {"detected": False, "duration": 0, "reason": "No work detected", "involved_nodes": []}

        # 2. Check for Continuity
        work_nodes.sort(key=lambda x: x[1])
        
        current_streak_start = work_nodes[0][1]
        current_streak_end = work_nodes[0][1]
        last_ts = work_nodes[0][1]
        current_streak_nodes = [work_nodes[0][0]]
        
        for i in range(1, len(work_nodes)):
            node, ts = work_nodes[i]
            gap = (ts - last_ts).total_seconds() / 60
            
            if gap > 15: # Break detected (or just gap in logs)
                # Check if previous streak was long enough
                duration = (current_streak_end - current_streak_start).total_seconds() / 60
                if duration > threshold_minutes:
                    return {
                        "detected": True, 
                        "duration": int(duration), 
                        "reason": f"Continuous work session of {int(duration)}m detected without significant breaks.",
                        "involved_nodes": current_streak_nodes
                    }
                # Reset streak
                current_streak_start = ts
                current_streak_nodes = []
            
            current_streak_nodes.append(node)
            current_streak_end = ts
            last_ts = ts
            
        # Check final streak
        duration = (current_streak_end - current_streak_start).total_seconds() / 60
        # print(f"[DEBUG] Final streak duration: {duration}m")
        if duration > threshold_minutes:
            return {
                "detected": True, 
                "duration": int(duration), 
                "reason": f"Continuous work session of {int(duration)}m detected without significant breaks.",
                "involved_nodes": current_streak_nodes
            }

        return {"detected": False, "duration": int(duration), "reason": "Work sessions are within safe limits", "involved_nodes": []}

    def detect_mixed_media_pattern(self) -> Dict[str, Any]:
        """
        Detects 'Mixed Media': Work followed by Entertainment (Eye strain risk).
        """
        # Look for Work -> Entertainment transition
        for u, v, data in self.graph.edges(data=True):
            if data.get("relation") == "NEXT":
                node_u = self.graph.nodes[u]
                node_v = self.graph.nodes[v]
                
                # Use regex for robust matching
                import re
                
                text_u = (node_u.get("statement", "")).lower()
                text_v = (node_v.get("statement", "")).lower()
                
                work_pattern = r"code|coding|debug|work|writing|implement"
                ent_pattern = r"youtube|video|movie|game|netflix"
                
                is_work_u = bool(re.search(work_pattern, text_u))
                is_ent_v = bool(re.search(ent_pattern, text_v))
                
                if is_work_u and is_ent_v:
                     return {
                        "detected": True,
                        "reason": "Transitioned from Work to Entertainment. Mental fatigue may drop, but Eye Strain/Sedentary risk remains high.",
                        "involved_nodes": [u, v]
                    }
                    
        return {"detected": False, "reason": "", "involved_nodes": []}

# Global Instance
graph_service = GraphService()
