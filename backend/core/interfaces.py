from abc import ABC, abstractmethod
from typing import Dict, Any
from .events import VitalEventBus, Event, EventType

class BaseSensor(ABC):
    """
    Abstract base class for all Input Plugins (Sensors).
    Examples: TwitterSensor, ScreenObserver, SmartWatchSensor.
    """
    def __init__(self, name: str, event_bus: VitalEventBus):
        self.name = name
        self.event_bus = event_bus
        self.is_running = False

    async def emit_data(self, data: Dict[str, Any]):
        """
        Helper to publish DATA_INGESTED events.
        """
        event = Event(
            type=EventType.DATA_INGESTED,
            payload=data,
            source=self.name
        )
        await self.event_bus.publish(event)

    @abstractmethod
    async def start(self):
        """Start the sensor loop."""
        pass

    @abstractmethod
    async def stop(self):
        """Stop the sensor loop."""
        pass

class BaseActuator(ABC):
    """
    Abstract base class for all Output Plugins (Actuators).
    Examples: DesktopNotifier, SmartLightController, ReportGenerator.
    """
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    async def execute(self, action_plan: Dict[str, Any]):
        """
        Execute the action requested by the Agent Council.
        """
        pass
