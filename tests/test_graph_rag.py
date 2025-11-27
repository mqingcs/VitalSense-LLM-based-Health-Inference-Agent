import sys
import os
import asyncio
import json
from unittest.mock import MagicMock, AsyncMock
from datetime import datetime, timedelta

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.core.graph_service import graph_service, GRAPH_FILE
from backend.core.enricher import graph_enricher
from backend.agents.schemas import MemoryEntry

# Override graph file path for testing
TEST_GRAPH_FILE = "backend/data/test_knowledge_graph.json"
import backend.core.graph_service
backend.core.graph_service.GRAPH_FILE = TEST_GRAPH_FILE

async def test_graph_rag():
    print("\n--- Testing GraphRAG & Persistence ---")
    
    # 1. Setup Mock Enricher
    # We want to simulate: "I am coding" -> Activity: "Coding"
    async def mock_enrich(text):
        if "coding" in text:
            return {
                "nodes": [{"id": "act_coding", "type": "Activity", "label": "Coding"}],
                "edges": [{"source": "mem_id", "target": "act_coding", "relation": "INVOLVES"}]
            }
        return {"nodes": [], "edges": []}
    
    graph_enricher.enrich_memory = AsyncMock(side_effect=mock_enrich)
    
    # 2. Add Memories (Simulate 2 hours of coding)
    print("Adding memories...")
    base_time = datetime.now() - timedelta(hours=2)
    
    memories = []
    for i in range(5):
        ts = base_time + timedelta(minutes=30*i)
        mem = MemoryEntry(
            id=f"mem_{i}",
            timestamp=ts.isoformat(),
            statement="I am coding the backend.",
            scene="Office",
            outcome="Progress",
            entities=[],
            user_state="active",
            remarks=""
        )
        await graph_service.add_memory_node(mem)
        memories.append(mem)
        
    # 3. Verify Persistence
    if os.path.exists(TEST_GRAPH_FILE):
        print("SUCCESS: Graph file created.")
    else:
        print("FAIL: Graph file not created.")
        return

    # 4. Verify Grind Detection
    print("Running Grind Detection...")
    result = graph_service.detect_grind_pattern(threshold_minutes=60)
    print(f"Result: {result}")
    
    if result["detected"]:
        print(f"SUCCESS: Detected grind. Duration: {result['duration']}m")
    else:
        print("FAIL: Did not detect grind.")

    # 5. Clean up
    if os.path.exists(TEST_GRAPH_FILE):
        os.remove(TEST_GRAPH_FILE)

if __name__ == "__main__":
    asyncio.run(test_graph_rag())
