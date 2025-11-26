import subprocess
import screen_brightness_control as sbc
from backend.core.interfaces import BaseActuator
from backend.agents.schemas import CouncilActionPlan

class NotificationActuator(BaseActuator):
    def __init__(self):
        super().__init__("SystemNotifier")

    async def execute(self, plan: CouncilActionPlan):
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

class BrightnessActuator(BaseActuator):
    def __init__(self):
        super().__init__("BrightnessControl")

    async def execute(self, target_brightness: int):
        try:
            # sbc.set_brightness(target_brightness)
            # For safety/demo, we just print if it fails (e.g. external monitor issues)
            sbc.set_brightness(target_brightness)
            print(f"[Actuator] Screen Brightness set to {target_brightness}%")
        except Exception as e:
            print(f"[Actuator] Brightness Control Failed (Permissions/Hardware): {e}")
