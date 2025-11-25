import asyncio
import random
from backend.core.interfaces import BaseSensor
from backend.core.events import VitalEventBus

SCENARIOS = [
    {"text": "User is scrolling Twitter at 2 AM. Keywords: 'insomnia', 'anxious'.", "type": "social_media"},
    {"text": "Screen shows code editor for 6 hours straight. No breaks.", "type": "screen_observer"},
    {"text": "User ordered 'Double Cheeseburger' via delivery app.", "type": "screen_observer"},
    {"text": "Wearable reports heart rate 110bpm while sitting.", "type": "wearable"},
]

class MockSensor(BaseSensor):
    """
    Simulates incoming data from various sources to test the Agent Council.
    """
    def __init__(self, event_bus: VitalEventBus):
        super().__init__("MockSensor", event_bus)

    async def start(self):
        self.is_running = True
        print(f"[{self.name}] Started. Emitting events every 10 seconds...")
        asyncio.create_task(self._loop())

    async def stop(self):
        self.is_running = False
        print(f"[{self.name}] Stopped.")

    async def _loop(self):
        while self.is_running:
            await asyncio.sleep(10) # Emit every 10s
            data = random.choice(SCENARIOS)
            print(f"[{self.name}] Detected: {data['text']}")
            await self.emit_data(data)
