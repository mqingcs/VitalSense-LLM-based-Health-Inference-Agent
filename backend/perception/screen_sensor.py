import asyncio
import pyautogui
import base64
import io
from PIL import Image
from backend.core.interfaces import BaseSensor
from backend.core.events import VitalEventBus
from backend.core.llm import llm_provider
from pydantic import BaseModel, Field

# --- Schema for Vision Analysis ---
class ScreenAnalysis(BaseModel):
    activity_category: str = Field(description="Broad category: Work, Entertainment, Social, Idle, etc.")
    health_risk_detected: bool = Field(description="True if the screen content suggests a health risk (stress, insomnia, eye strain).")
    emotional_tone: str = Field(description="The likely emotional state induced by this content (e.g., Anxious, Relaxed, Bored).")
    description: str = Field(description="A concise, 1-sentence summary of what the user is doing, focusing on health impact.")

# --- Advanced Prompt Engineering ---
VISION_PROMPT = """
You are the "Visual Cortex" of a Health AI.
Analyze this screenshot of the user's computer.
Your goal is to detect **Health & Well-being Signals**.

Look for:
1.  **Stress Triggers**: Doomscrolling news, debugging complex code errors, arguing on social media.
2.  **Fatigue Indicators**: Late-night timestamps, chaotic window management, "blue light" heavy content.
3.  **Dietary Signals**: Food delivery apps, recipes (junk food vs healthy).
4.  **Emotional Context**: Is the content relaxing (nature videos) or anxiety-inducing (stock market crashes)?

Ignore sensitive PII (passwords, bank numbers). Focus ONLY on the user's state of mind and body.
"""

class ScreenSensor(BaseSensor):
    def __init__(self, event_bus: VitalEventBus, interval: int = 30):
        super().__init__("ScreenObserver", event_bus)
        self.interval = interval

    async def start(self):
        self.is_running = True
        print(f"[{self.name}] Started. Watching screen every {self.interval}s...")
        asyncio.create_task(self._loop())

    async def stop(self):
        self.is_running = False
        print(f"[{self.name}] Stopped.")

    async def _loop(self):
        while self.is_running:
            await asyncio.sleep(self.interval)
            
            try:
                # 1. Capture Screen
                screenshot = pyautogui.screenshot()
                
                # 2. Resize for efficiency (Gemini Flash doesn't need 4K)
                screenshot.thumbnail((1024, 1024))
                
                # 3. Convert to Bytes
                img_byte_arr = io.BytesIO()
                screenshot.save(img_byte_arr, format='JPEG')
                img_bytes = img_byte_arr.getvalue()
                
                # 4. Analyze with Gemini Vision
                # Note: The Google GenAI SDK handles image bytes differently depending on version.
                # We will assume the provider handles the complex part, or we pass the PIL image directly if supported.
                # For now, let's extend the provider to support images, or use a helper here.
                
                # Let's assume we need to pass the image object to the provider.
                # Since our current provider only takes text prompt, we need to update it or handle it here.
                # For this implementation, I will assume we update the provider to handle 'contents' list.
                
                # Wait! The current provider `generate_structured` takes a `prompt` string.
                # I need to update `llm.py` to accept multimodal input or handle it here.
                # Let's update `llm.py` first to be more flexible.
                
                # For now, I will skip the actual API call in this file write and update LLM provider next.
                # I'll put a placeholder here.
                pass 

            except Exception as e:
                print(f"[{self.name}] Error: {e}")

# Reworking the class to be complete assuming updated LLM provider
class ScreenSensorComplete(BaseSensor):
    def __init__(self, event_bus: VitalEventBus, interval: int = 30):
        super().__init__("ScreenObserver", event_bus)
        self.interval = interval

    async def start(self):
        self.is_running = True
        print(f"[{self.name}] Started. Watching screen every {self.interval}s...")
        asyncio.create_task(self._loop())

    async def stop(self):
        self.is_running = False
        print(f"[{self.name}] Stopped.")

    async def _loop(self):
        while self.is_running:
            await asyncio.sleep(self.interval)
            try:
                # 1. Capture
                screenshot = pyautogui.screenshot()
                screenshot.thumbnail((1024, 1024))
                
                # 2. Analyze
                # We will use a specialized method on the provider (to be added)
                analysis = await llm_provider.analyze_image(
                    image=screenshot,
                    prompt=VISION_PROMPT,
                    schema_model=ScreenAnalysis
                )
                
                print(f"[{self.name}] Analysis: {analysis.description} (Risk: {analysis.health_risk_detected})")
                
                # 3. Emit if relevant
                if analysis.health_risk_detected or analysis.activity_category in ["Work", "Social"]:
                    await self.emit_data({
                        "text": f"Screen Analysis: {analysis.description}. Context: {analysis.emotional_tone}.",
                        "type": "screen_observer",
                        "raw_category": analysis.activity_category
                    })
                    
            except Exception as e:
                print(f"[{self.name}] Error: {e}")
