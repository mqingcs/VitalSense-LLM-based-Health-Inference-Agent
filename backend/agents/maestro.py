from pydantic import BaseModel, Field
from backend.core.llm import llm_provider

class EnvironmentState(BaseModel):
    hex_color: str = Field(description="Hex color code for the ambient background (e.g. #00FFFF).")
    turbulence: float = Field(description="0.0 (Calm) to 1.0 (Chaotic). Controls shader noise.")
    speed: float = Field(description="0.1 (Slow) to 2.0 (Fast). Controls animation speed.")
    brightness: int = Field(description="Target screen brightness (0-100).")
    reasoning: str = Field(description="Why this environment was chosen.")

MAESTRO_PROMPT = """
You are Maestro, the Environmental Controller for VitalOS.
Your job is to optimize the user's physical and digital environment based on their state.

**Input:**
Risk Level: {risk_level}
Emotional Tone: {emotional_tone}
Activity: {activity}

**Guidelines:**
1.  **High Stress / Anxiety**:
    - Color: Cool Blues/Greens (Calming) OR Warm Orange (Cozy). Avoid aggressive Red.
    - Turbulence: Low (0.1). Smooth, flowing.
    - Speed: Slow (0.2).
    - Brightness: Lower (60-70) to reduce stimulation.

2.  **High Focus / Flow**:
    - Color: Deep Indigo/Purple.
    - Turbulence: Medium (0.4). Steady energy.
    - Speed: Medium (0.5).
    - Brightness: Optimal (80).

3.  **Fatigue / Eye Strain**:
    - Color: Warm Amber/Sepia (Blue light reduction vibe).
    - Turbulence: Very Low (0.05).
    - Speed: Very Slow (0.1).
    - Brightness: Dim (40-50).

4.  **High Risk (Emergency)**:
    - Color: Pulsing Red/Alert.
    - Turbulence: High (0.8).
    - Speed: Fast (1.5).
    - Brightness: High (100) to alert, OR Dim if it's a migraine. Use judgement.

Output the JSON `EnvironmentState`.
"""

async def run_maestro(risk_level: str, emotional_tone: str, activity: str) -> EnvironmentState:
    context = f"Risk Level: {risk_level}\nEmotional Tone: {emotional_tone}\nActivity: {activity}"
    try:
        result = await llm_provider.generate_structured(
            prompt=MAESTRO_PROMPT,
            schema_model=EnvironmentState,
            context=context
        )
        return result
    except Exception as e:
        print(f"[Maestro] Error: {e}")
        return EnvironmentState(
            hex_color="#000000", 
            turbulence=0.1, 
            speed=0.1, 
            brightness=80, 
            reasoning="Fallback"
        )
