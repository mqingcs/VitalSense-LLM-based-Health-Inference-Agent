from backend.agents.schemas import MemoryEntry

def test_memory_entry_validation():
    print("\n--- Testing MemoryEntry Validation ---")
    
    # Simulate legacy data (missing 'remarks')
    legacy_data = {
        "timestamp": "2023-10-27T10:00:00",
        "scene": "Work",
        "statement": "Coding python",
        "entities": ["Python"],
        "user_state": "Focused",
        "outcome": "Progress"
    }
    
    try:
        entry = MemoryEntry(**legacy_data)
        print("SUCCESS: MemoryEntry instantiated without 'remarks'.")
        print(f"Remarks value: {entry.remarks}")
        assert entry.remarks is None
    except Exception as e:
        print(f"FAILURE: Validation error: {e}")

if __name__ == "__main__":
    test_memory_entry_validation()
