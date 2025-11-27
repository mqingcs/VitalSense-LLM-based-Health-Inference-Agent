import sys
import os
import asyncio
from unittest.mock import MagicMock

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.core.pulse import vital_pulse
from backend.agents.liaison import fetch_profile_context

def test_pulse_logic():
    print("\n--- Testing VitalPulse Logic ---")
    
    # Mock time to be way in the future so check triggers
    import time
    now = time.time()
    
    # Force trigger hydration check
    # We mock _get_last_event_time to return 5 hours ago
    vital_pulse._get_last_event_time = MagicMock(return_value=now - (3600 * 5))
    
    # Mock socket manager
    from unittest.mock import AsyncMock
    mock_socket = MagicMock()
    mock_socket.emit = AsyncMock()
    vital_pulse.socket_manager = mock_socket
    
    # Run the beat logic synchronously for test
    # Since _beat is async, we need an event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    print("Running Pulse Beat...")
    loop.run_until_complete(vital_pulse._beat())
    
    # Check if emit was called
    if mock_socket.emit.called:
        args = mock_socket.emit.call_args
        print(f"SUCCESS: Pulse triggered intervention: {args}")
    else:
        print("FAIL: Pulse did not trigger intervention.")

def test_on_demand_context():
    print("\n--- Testing On-Demand Context Tool ---")
    
    # Test fetching habits
    result = fetch_profile_context.invoke({"category": "habits"})
    print(f"Result for 'habits': {result}")
    
    if "Habits:" in result:
        print("SUCCESS: Fetched habits.")
    else:
        print("FAIL: Did not fetch habits.")

if __name__ == "__main__":
    test_pulse_logic()
    test_on_demand_context()
