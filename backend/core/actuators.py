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
            
            # 1. System Notification (OS Level)
            # Escape quotes for AppleScript
            safe_message = message.replace('"', '\\"')
            safe_title = title.replace('"', '\\"')
            cmd = f'display notification "{safe_message}" with title "{safe_title}" sound name "Ping"'
            
            try:
                subprocess.run(["osascript", "-e", cmd], check=True)
                print(f"[{self.name}] Notification sent: {title}")
            except Exception as e:
                print(f"[{self.name}] Failed to send notification: {e}")

            # 2. Interactive Card (Frontend Level)
            # We need to access the socket manager. Ideally injected, but for now we can try to import
            # or rely on the main loop to emit. 
            # Actually, main.py calls this actuator. 
            # Let's return the card data so main.py can emit it, OR we can try to emit here if we had the socket.
            # Given the architecture, main.py already emits 'intervention'. 
            # We should update main.py to emit 'risk_card' instead of generic 'intervention' or include the card data.
            
            # Let's assume main.py handles the emission if we return data, OR we update main.py.
            # Checking main.py: It calls `await notifier.execute(final_plan)` then `await sio.emit('intervention', final_data)`.
            # So we don't need to emit here. We just need to ensure 'intervention' event has the right structure for the card.
            pass

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
