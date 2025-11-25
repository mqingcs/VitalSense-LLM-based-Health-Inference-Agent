import subprocess
from backend.core.interfaces import BaseActuator
from backend.agents.schemas import CouncilActionPlan

class NotificationActuator(BaseActuator):
    """
    Actuator that triggers a native OS notification (macOS).
    """
    def __init__(self):
        super().__init__("SystemNotifier")

    async def execute(self, plan: CouncilActionPlan):
        """
        Displays a notification if the risk is HIGH.
        """
        if plan.risk_level == "HIGH":
            title = "VitalOS Alert: HIGH RISK"
            message = f"{plan.summary} Advice: {plan.actions[0] if plan.actions else 'Take a break.'}"
            
            # Escape quotes for AppleScript
            message = message.replace('"', '\\"')
            title = title.replace('"', '\\"')
            
            cmd = f'display notification "{message}" with title "{title}" sound name "Ping"'
            
            try:
                subprocess.run(["osascript", "-e", cmd], check=True)
                print(f"[{self.name}] Notification sent: {title}")
            except Exception as e:
                print(f"[{self.name}] Failed to send notification: {e}")
