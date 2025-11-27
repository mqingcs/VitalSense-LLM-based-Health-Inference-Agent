import chromadb
import uuid
import json
from datetime import datetime
from typing import List, Dict, Any
from backend.core.llm import llm_provider
from backend.agents.schemas import MemoryEntry
from backend.core.graph_service import graph_service

class Hippocampus:
    """
    The Long-term Memory System of VitalOS.
    Uses ChromaDB to store and retrieve 'Health Episodes'.
    """
    def __init__(self):
        # Persistent local storage
        self.client = chromadb.PersistentClient(path="backend/data/chroma")
        self.collection = self.client.get_or_create_collection(name="health_episodes")

    async def add_memory(self, full_log: str):
        """
        Extracts structure, embeds summary, and stores in ChromaDB.
        """
        try:
            # 1. Extract Structure (GraphRAG Ready)
            entry: MemoryEntry = await llm_provider.extract_memory_dimensions(full_log)
            
            # 2. Generate Summary for Indexing
            # We use the 'statement' + 'scene' + 'outcome' as the semantic index
            index_text = f"{entry.scene}: {entry.statement}. Result: {entry.outcome}"
            
            # 3. Generate Embedding
            embedding = await llm_provider.get_embedding(index_text)
            
            if not embedding:
                print("[Hippocampus] Failed to generate embedding. Skipping.")
                return

            # 4. Store
            # ChromaDB metadata cannot hold lists or None. We must serialize/filter them.
            metadata = json.loads(entry.model_dump_json())
            clean_metadata = {}
            for key, value in metadata.items():
                if value is None:
                    continue # Skip None values (ChromaDB doesn't support them)
                if isinstance(value, list):
                    clean_metadata[key] = json.dumps(value)
                else:
                    clean_metadata[key] = value
            
            self.collection.add(
                documents=[index_text],
                embeddings=[embedding],
                metadatas=[clean_metadata], 
                ids=[str(uuid.uuid4())]
            )
            print(f"[Hippocampus] Memory Stored: {entry.statement}")
            
            # 5. Update Knowledge Graph (GraphRAG)
            await graph_service.add_memory_node(entry)
            
        except Exception as e:
            print(f"[Hippocampus] Error adding memory: {e}")

    async def recall(self, query: str, k: int = 3) -> List[MemoryEntry]:
        """
        Retrieves relevant past memories based on semantic similarity.
        """
        try:
            # 1. Embed Query
            embedding = await llm_provider.get_embedding(query)
            if not embedding:
                return []
            
            # 2. Search
            results = self.collection.query(
                query_embeddings=[embedding],
                n_results=k
            )
            
            memories = []
            if results['metadatas']:
                for meta in results['metadatas'][0]:
                    # Deserialize lists (ChromaDB stores them as strings)
                    for key, value in meta.items():
                        if isinstance(value, str) and value.startswith("[") and value.endswith("]"):
                            try:
                                meta[key] = json.loads(value)
                            except json.JSONDecodeError:
                                pass
                                
                    # Reconstruct Pydantic model from metadata
                    memories.append(MemoryEntry(**meta))
                    
            print(f"[Hippocampus] Recalled {len(memories)} memories.")
            return memories
            
        except Exception as e:
            print(f"[Hippocampus] Error recalling memory: {e}")
            return []

            return memories
        except Exception as e:
            print(f"[Hippocampus] Error fetching all memories: {e}")
            return []

    async def delete_memory(self, memory_id: str):
        """
        Deletes a specific memory by ID.
        """
        try:
            self.collection.delete(ids=[memory_id])
            print(f"[Hippocampus] Deleted memory: {memory_id}")
            return True
        except Exception as e:
            print(f"[Hippocampus] Error deleting memory {memory_id}: {e}")
            return False

    async def clear_all(self):
        """
        Deletes ALL memories.
        """
        try:
            # ChromaDB doesn't have a truncate, so we get all IDs and delete
            all_ids = self.collection.get()['ids']
            if all_ids:
                self.collection.delete(ids=all_ids)
            print(f"[Hippocampus] Cleared all memories.")
            return True
        except Exception as e:
            print(f"[Hippocampus] Error clearing all memories: {e}")
            return False

    async def delete_range(self, start_iso: str, end_iso: str):
        """
        Deletes memories within a time range.
        """
        try:
            # Use metadata filtering
            self.collection.delete(
                where={
                    "$and": [
                        {"timestamp": {"$gte": start_iso}},
                        {"timestamp": {"$lte": end_iso}}
                    ]
                }
            )
            print(f"[Hippocampus] Deleted memories between {start_iso} and {end_iso}")
            return True
        except Exception as e:
            print(f"[Hippocampus] Error deleting range: {e}")
            return False

    async def get_all_memories(self) -> List[MemoryEntry]:
        """
        Retrieves ALL memories for the 3D Graph.
        """
        try:
            results = self.collection.get()
            memories = []
            
            print(f"[Hippocampus] Raw results count: {len(results['ids']) if results['ids'] else 0}")
            
            if results['metadatas']:
                for i, meta in enumerate(results['metadatas']):
                    # Deserialize lists
                    for key, value in meta.items():
                        if isinstance(value, str) and value.startswith("[") and value.endswith("]"):
                            try:
                                meta[key] = json.loads(value)
                            except json.JSONDecodeError:
                                pass
                    
                    # Inject ID
                    try:
                        entry = MemoryEntry(**meta)
                        entry.id = results['ids'][i]
                        memories.append(entry)
                    except Exception as e:
                         print(f"[Hippocampus] Failed to parse memory {results['ids'][i]}: {e}")

            print(f"[Hippocampus] Returning {len(memories)} valid memories.")
            return memories
        except Exception as e:
            print(f"[Hippocampus] Error fetching all memories: {e}")
            return []

    async def get_debug_stats(self):
        """
        Returns raw stats from ChromaDB.
        """
        try:
            count = self.collection.count()
            peek = self.collection.peek(limit=1)
            return {
                "count": count,
                "peek_ids": peek['ids'],
                "peek_metadatas": peek['metadatas']
            }
        except Exception as e:
            return {"error": str(e)}

# Global Instance
hippocampus = Hippocampus()
