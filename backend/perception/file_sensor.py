import asyncio
import json
import os
from backend.core.interfaces import BaseSensor
from backend.core.events import VitalEventBus

INPUT_FILE = "backend/data/input.json"

class FileSensor(BaseSensor):
    """
    Watches a local JSON file for changes.
    Useful for simulating external data (Wearables, Social Media) during demos.
    """
    def __init__(self, event_bus: VitalEventBus):
        super().__init__("FileIngestor", event_bus)
        self.last_mtime = 0

    async def start(self):
        self.is_running = True
        # Ensure directory exists
        os.makedirs(os.path.dirname(INPUT_FILE), exist_ok=True)
        if not os.path.exists(INPUT_FILE):
            with open(INPUT_FILE, "w") as f:
                json.dump({"text": "Initial state", "type": "system"}, f)
        
        print(f"[{self.name}] Started. Watching {INPUT_FILE}...")
        asyncio.create_task(self._loop())

    async def stop(self):
        self.is_running = False
        print(f"[{self.name}] Stopped.")

    async def _loop(self):
        while self.is_running:
            await asyncio.sleep(1) # Check every second
            try:
                if not os.path.exists(INPUT_FILE):
                    continue
                
                mtime = os.path.getmtime(INPUT_FILE)
                if mtime > self.last_mtime:
                    self.last_mtime = mtime
                    
                    # Read file
                    with open(INPUT_FILE, "r") as f:
                        data = json.load(f)
                    
                    # If it's a valid event, emit it
                    if "text" in data and "type" in data:
                        print(f"[{self.name}] New Data Detected: {data['text']}")
                        await self.emit_data(data)
                        
            except Exception as e:
                print(f"[{self.name}] Error: {e}")
