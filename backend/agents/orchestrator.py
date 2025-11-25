from typing import TypedDict, Annotated, List, Union
from langgraph.graph import StateGraph, END
import operator

# --- 1. Define the "VitalState" ---
# This is the shared memory of the Council.
class VitalState(TypedDict):
    user_id: str
    input_data: str  # Raw text/image description from Perception Layer
    source: str      # "social_media", "screen_observer", "wearable"
    
    # The "Council's" Analysis
    medical_risk_score: float
    lifestyle_risk_score: float
    
    # The Debate Log
    council_discussion: Annotated[List[str], operator.add]
    
    # Final Decision
    action_plan: str

# --- 2. Define the Agents (Nodes) ---

def triage_agent(state: VitalState):
    """
    The Gatekeeper. Decides which experts are needed.
    """
    print(f"--- [Triage] Analyzing signal from {state['source']} ---")
    # Logic: If medical keywords -> Doctor. If habit keywords -> Coach.
    # For now, we simulate passing to both.
    return {"council_discussion": ["Triage: Signal detected. Convening Council."]}

def medical_analyst(state: VitalState):
    """
    'Dr. Nexus': Analyzes clinical risks.
    """
    print("--- [Dr. Nexus] Reviewing clinical markers ---")
    return {
        "medical_risk_score": 0.2, # Placeholder
        "council_discussion": ["Dr. Nexus: No immediate acute symptoms detected."]
    }

def lifestyle_coach(state: VitalState):
    """
    'Guardian': Analyzes behavioral patterns.
    """
    print("--- [Guardian] Reviewing lifestyle patterns ---")
    return {
        "lifestyle_risk_score": 0.5, # Placeholder
        "council_discussion": ["Guardian: User has been sedentary for 4 hours."]
    }

def synthesizer(state: VitalState):
    """
    The Chair. Synthesizes the debate into an Action Plan.
    """
    print("--- [Synthesizer] Formulating Action Plan ---")
    return {"action_plan": "Recommendation: Trigger 'Stand Up' alert on VitalOverlay."}

# --- 3. Build the Graph ---

workflow = StateGraph(VitalState)

# Add Nodes
workflow.add_node("triage", triage_agent)
workflow.add_node("doctor", medical_analyst)
workflow.add_node("coach", lifestyle_coach)
workflow.add_node("synthesizer", synthesizer)

# Define Edges
workflow.set_entry_point("triage")
workflow.add_edge("triage", "doctor")
workflow.add_edge("triage", "coach")
workflow.add_edge("doctor", "synthesizer")
workflow.add_edge("coach", "synthesizer")
workflow.add_edge("synthesizer", END)

# Compile
app = workflow.compile()
