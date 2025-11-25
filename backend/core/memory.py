import chromadb
import uuid
import json
from datetime import datetime
from typing import List, Dict, Any
from backend.core.llm import llm_provider
from backend.agents.schemas import MemoryEntry

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
            # ChromaDB metadata cannot hold lists. We must serialize them.
            metadata = json.loads(entry.model_dump_json())
            for key, value in metadata.items():
                if isinstance(value, list):
                    metadata[key] = json.dumps(value)
            
            self.collection.add(
                documents=[index_text],
                embeddings=[embedding],
                metadatas=[metadata], 
                ids=[str(uuid.uuid4())]
            )
            print(f"[Hippocampus] Memory Stored: {entry.statement}")
            
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

    async def get_all_memories(self) -> List[MemoryEntry]:
        """
        Retrieves ALL memories for the 3D Graph.
        """
        try:
            results = self.collection.get()
            memories = []
            
            if results['metadatas']:
                for meta in results['metadatas']:
                    # Deserialize lists
                    for key, value in meta.items():
                        if isinstance(value, str) and value.startswith("[") and value.endswith("]"):
                            try:
                                meta[key] = json.loads(value)
                            except json.JSONDecodeError:
                                pass
                    memories.append(MemoryEntry(**meta))
            
            return memories
        except Exception as e:
            print(f"[Hippocampus] Error fetching all memories: {e}")
            return []

# Global Instance
hippocampus = Hippocampus()
