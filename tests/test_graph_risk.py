import unittest
from datetime import datetime, timedelta
from backend.core.graph_service import GraphService
from backend.agents.schemas import MemoryEntry

class TestGraphRisk(unittest.TestCase):
    def setUp(self):
        self.graph_service = GraphService()

    def create_memory(self, statement: str, minutes_ago: int, entities: list = []):
        ts = (datetime.now() - timedelta(minutes=minutes_ago)).isoformat()
        return MemoryEntry(
            timestamp=ts,
            statement=statement,
            scene="Test Scene",
            entities=entities,
            user_state="Neutral",
            outcome="None",
            remarks="Test remark",
            id=f"mem_{minutes_ago}"
        )

    def test_grind_detection(self):
        # Scenario: 70 minutes of continuous coding
        memories = [
            self.create_memory("Started coding login", 70, ["VS Code"]),
            self.create_memory("Debugging auth bug", 60, ["VS Code"]),
            self.create_memory("Still debugging", 50, ["VS Code"]),
            self.create_memory("Writing tests", 40, ["VS Code"]),
            self.create_memory("Refactoring", 30, ["VS Code"]),
            self.create_memory("Committing code", 20, ["Git"]),
            self.create_memory("Deploying", 10, ["Terminal"]),
        ]
        
        self.graph_service.build_graph(memories)
        result = self.graph_service.detect_grind_pattern(threshold_minutes=45)
        
        print(f"\n[Test Grind] Result: {result}")
        self.assertTrue(result["detected"])
        self.assertIn("Continuous work", result["reason"])

    def test_break_detection(self):
        # Scenario: Coding -> Break -> Coding
        memories = [
            self.create_memory("Coding", 70, ["VS Code"]),
            self.create_memory("Coding", 60, ["VS Code"]),
            # GAP of 30 mins
            self.create_memory("Coding", 30, ["VS Code"]),
            self.create_memory("Coding", 20, ["VS Code"]),
        ]
        
        self.graph_service.build_graph(memories)
        result = self.graph_service.detect_grind_pattern(threshold_minutes=45)
        
        print(f"\n[Test Break] Result: {result}")
        # Should be False because the longest streak is ~30 mins (70-60=10, 30-20=10)
        # Wait, my logic in detect_grind_pattern groups by gap > 15m.
        # 70->60 (gap 10). Streak 10m.
        # 60->30 (gap 30). Break. Reset.
        # 30->20 (gap 10). Streak 10m.
        # Max streak 10m < 45m.
        self.assertFalse(result["detected"])

    def test_mixed_media(self):
        # Scenario: Coding -> YouTube
        memories = [
            self.create_memory("Finished coding", 10, ["VS Code"]),
            self.create_memory("Watching tech talk on YouTube", 5, ["YouTube"]),
        ]
        
        self.graph_service.build_graph(memories)
        result = self.graph_service.detect_mixed_media_pattern()
        
        print(f"\n[Test Mixed] Result: {result}")
        self.assertTrue(result["detected"])
        self.assertIn("Work to Entertainment", result["reason"])

if __name__ == '__main__':
    unittest.main()
