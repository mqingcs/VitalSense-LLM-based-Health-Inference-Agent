import asyncio
from typing import Callable, Dict, List, Any, Awaitable
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime

class EventType(Enum):
    SYSTEM_STARTUP = "system.startup"
    DATA_INGESTED = "data.ingested"      # Raw data from sensors
    ANALYSIS_COMPLETED = "analysis.completed" # Agent output
    ACTION_REQUIRED = "action.required"  # Actuator trigger
    ERROR = "system.error"

@dataclass
class Event:
    type: EventType
    payload: Dict[str, Any]
    source: str
    timestamp: datetime = field(default_factory=datetime.now)

class VitalEventBus:
    """
    The Central Nervous System of VitalOS.
    Handles async event dispatching between Sensors, Agents, and Actuators.
    """
    def __init__(self):
        self._subscribers: Dict[EventType, List[Callable[[Event], Awaitable[None]]]] = {}

    def subscribe(self, event_type: EventType, callback: Callable[[Event], Awaitable[None]]):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(callback)
        print(f"[EventBus] Subscribed to {event_type.value}")

    async def publish(self, event: Event):
        print(f"[EventBus] Publishing {event.type.value} from {event.source}")
        if event.type in self._subscribers:
            # Run all callbacks concurrently
            await asyncio.gather(*[cb(event) for cb in self._subscribers[event.type]])

# Global Singleton
event_bus = VitalEventBus()
