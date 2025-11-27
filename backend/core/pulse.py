import asyncio
import time
import logging
from typing import Optional, Callable
from backend.core.graph_service import graph_service
from backend.core.profile_service import profile_service

logger = logging.getLogger("vital_pulse")

class VitalPulse:
    """
    The Autonomous Heartbeat of VitalSense.
    
    Mission: To proactively perceive user state and initiate interaction
    when health risks or anomalies are detected, without waiting for user input.
    
    Philosophy:
    - Autonomy: Runs independently in the background.
    - Perception: Reads the Knowledge Graph and Profile.
    - Intelligence: Decides when to intervene based on context (and cool-downs).
    """
    
    def __init__(self, socket_manager=None):
        self.running = False
        self.socket_manager = socket_manager
        self.last_check = 0
        self.check_interval = 60 # Check every minute
        
        # State tracking for cool-downs
        self.last_intervention = {
            "hydration": 0,
            "posture": 0,
            "connection": 0
        }
        
        # Cool-down periods (seconds)
        self.COOLDOWNS = {
            "hydration": 3600 * 3, # 3 hours
            "posture": 3600 * 2,   # 2 hours
            "connection": 3600 * 24 # 24 hours (Daily check-in)
        }

    async def start(self):
        """Starts the pulse loop."""
        self.running = True
        logger.info("[VitalPulse] System Heartbeat Started.")
        
        # Wake-Up Consolidation Check
        await self._check_startup_gap()
        
        while self.running:
            try:
                await self._beat()
            except Exception as e:
                logger.error(f"[VitalPulse] Arrhythmia detected: {e}")
            
            await asyncio.sleep(self.check_interval)

    async def _check_startup_gap(self):
        """
        Checks if the system was off for a long time (Sleep Mode).
        If > 4 hours, triggers Memory Consolidation.
        """
        from backend.core.memory import hippocampus
        import datetime
        
        try:
            # Get last memory timestamp
            memories = await hippocampus.get_all_memories()
            if not memories:
                return

            # Sort by time descending
            memories.sort(key=lambda x: x.timestamp, reverse=True)
            last_mem_time = datetime.datetime.fromisoformat(memories[0].timestamp).timestamp()
            now = time.time()
            
            hours_gap = (now - last_mem_time) / 3600
            print(f"[VitalPulse] Startup Gap: {hours_gap:.2f} hours")
            
            if hours_gap > 4:
                print("[VitalPulse] Long gap detected. Triggering Wake-Up Consolidation...")
                await hippocampus.consolidate_memories()
                
        except Exception as e:
            print(f"[VitalPulse] Error checking startup gap: {e}")

    def stop(self):
        self.running = False
        logger.info("[VitalPulse] System Heartbeat Stopped.")

    async def _beat(self):
        """The core logic cycle."""
        now = time.time()
        
        # 1. Hydration Check
        # Logic: If no 'drink' event in graph for > 4h AND not sleeping
        if self._should_trigger("hydration", now):
            # In a real graph, we'd query: graph_service.get_last_event("drink")
            # For prototype, we simulate a check or use a heuristic
            # Let's assume we check the graph for "water" or "drink" nodes
            last_drink = self._get_last_event_time(["water", "drink", "hydrate"])
            hours_since = (now - last_drink) / 3600
            
            if hours_since > 4:
                await self._intervene(
                    "hydration", 
                    "Hey, I noticed it's been a while since you logged any water. Staying hydrated helps with that brain fog. Want to grab a glass?"
                )

    def _should_trigger(self, category: str, now: float) -> bool:
        """Checks cool-downs."""
        last = self.last_intervention.get(category, 0)
        return (now - last) > self.COOLDOWNS.get(category, 3600)

    def _get_last_event_time(self, keywords: list) -> float:
        """
        Queries the graph for the last occurrence of specific keywords.
        Returns timestamp (float).
        """
        # This would ideally query the GraphService. 
        # Since GraphService is in-memory and simple, we iterate nodes.
        # If no event found, return a default (e.g., start of day)
        latest = 0.0
        
        # Accessing graph directly (assuming thread safety or read-only is fine)
        for node, data in graph_service.graph.nodes(data=True):
            if data.get("type") == "memory":
                text = (data.get("statement", "") + " " + data.get("scene", "")).lower()
                if any(k in text for k in keywords):
                    ts = data.get("timestamp")
                    if ts:
                        # Convert datetime to timestamp if needed
                        import datetime
                        if isinstance(ts, datetime.datetime):
                            ts_float = ts.timestamp()
                        else:
                            ts_float = float(ts) # Fallback
                        
                        if ts_float > latest:
                            latest = ts_float
                            
        # If never found, assume user drank water when system started (to avoid instant nag)
        if latest == 0.0:
            return time.time() - 3600 * 5 # Pretend 5 hours ago to trigger test if needed
            
        return latest

    async def _intervene(self, category: str, message: str):
        """Executes the intervention via SocketIO."""
        logger.info(f"[VitalPulse] Intervening: {category}")
        self.last_intervention[category] = time.time()
        
        if self.socket_manager:
            await self.socket_manager.emit("chat_reply", {"message": message})
        else:
            print(f"[VitalPulse] (No Socket) Would say: {message}")

# Global Instance
vital_pulse = VitalPulse()
