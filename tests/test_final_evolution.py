import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from backend.core.memory import hippocampus, MemoryEntry
from backend.core.risk_engine import risk_engine
from backend.core.profile_service import profile_service

async def test_wake_up_consolidation():
    print("\n--- Testing Wake-Up Consolidation ---")
    
    # Mock memories
    mock_memories = [
        MemoryEntry(id="1", timestamp="2023-10-27T10:00:00", statement="Coding python", scene="Work", outcome="Progress", entities=[], user_state="Focused", remarks=""),
        MemoryEntry(id="2", timestamp="2023-10-27T10:05:00", statement="Typing code", scene="Work", outcome="Progress", entities=[], user_state="Focused", remarks=""),
        MemoryEntry(id="3", timestamp="2023-10-27T10:10:00", statement="Debugging", scene="Work", outcome="Fix", entities=[], user_state="Focused", remarks=""),
        MemoryEntry(id="4", timestamp="2023-10-27T10:15:00", statement="Running tests", scene="Work", outcome="Pass", entities=[], user_state="Focused", remarks=""),
        MemoryEntry(id="5", timestamp="2023-10-27T10:20:00", statement="Commit changes", scene="Work", outcome="Done", entities=[], user_state="Focused", remarks="")
    ]
    
    # Mock Hippocampus methods
    with patch.object(hippocampus, 'get_all_memories', new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_memories
        
        with patch.object(hippocampus, 'add_memory', new_callable=AsyncMock) as mock_add:
            with patch.object(hippocampus.collection, 'delete') as mock_delete:
                # Mock LLM Summary
                with patch('backend.core.llm.llm_provider.summarize_day', new_callable=AsyncMock) as mock_summary:
                    mock_summary.return_value = "User spent the morning coding and debugging effectively."
                    
                    # Run Consolidation
                    await hippocampus.consolidate_memories()
                    
                    # Verify Summary Created
                    assert mock_summary.called
                    assert mock_add.called
                    args, _ = mock_add.call_args
                    assert "Summary of previous session" in args[0]
                    
                    # Verify Pruning
                    assert mock_delete.called
                    print("SUCCESS: Consolidation logic verified (Summary created, Raw deleted).")

async def test_interactive_feedback():
    print("\n--- Testing Interactive Feedback Loop ---")
    
    # 1. Baseline Tolerance
    profile_service.profile.risk_modifiers["sedentary"] = 1.0
    
    # 2. Simulate Dismissal (Adjust Tolerance)
    risk_engine.adjust_tolerance("sedentary", 0.1)
    
    # 3. Verify Tolerance Increased (Modifier Decreased)
    new_mod = profile_service.get_risk_modifier("sedentary")
    print(f"Old Modifier: 1.0 -> New Modifier: {new_mod}")
    assert new_mod == 0.9
    
    print("SUCCESS: Feedback loop verified.")

if __name__ == "__main__":
    asyncio.run(test_wake_up_consolidation())
    asyncio.run(test_interactive_feedback())
