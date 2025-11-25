from typing import Dict, Any, List
import json
from langgraph.graph import StateGraph, END
from backend.core.schema import AnalysisResult
from backend.agents.personas import TRIAGE_PROMPT, DOCTOR_PROMPT, COACH_PROMPT, SYNTHESIZER_PROMPT
from backend.core.llm import llm_provider
from backend.agents.schemas import TriageResult, RiskAssessment, CouncilActionPlan, MemoryEntry
from backend.core.memory import hippocampus

# --- State Definition ---
class CouncilState(Dict):
    input_data: str
    source: str
    past_memories: List[MemoryEntry] # [NEW] Context from Hippocampus
    triage_result: TriageResult
    doctor_output: RiskAssessment
    coach_output: RiskAssessment
    final_output: CouncilActionPlan

# --- Nodes ---
async def triage_node(state: CouncilState):
    print("--- [Council] Triage Agent Active ---")
    
    # 1. Recall Past Memories
    memories = await hippocampus.recall(state['input_data'])
    memory_context = "\n".join([f"- [{m.timestamp}] {m.statement}" for m in memories]) if memories else "None"
    
    context = f"Input: {state['input_data']}\nSource: {state['source']}\nPast History:\n{memory_context}"
    
    try:
        result = await llm_provider.generate_structured(
            prompt=TRIAGE_PROMPT,
            schema_model=TriageResult,
            context=context
        )
    except Exception:
        result = TriageResult(needs_doctor=True, needs_coach=True, reasoning="Error in Triage")
        
    return {"triage_result": result, "past_memories": memories}

async def doctor_node(state: CouncilState):
    print("--- [Council] Dr. Nexus Active ---")
    
    # Inject Memory
    memories = state.get("past_memories", [])
    memory_context = "\n".join([f"- {m.statement} (Outcome: {m.outcome})" for m in memories]) if memories else "None"
    
    context = f"Input: {state['input_data']}\nPatient History:\n{memory_context}"
    
    try:
        result = await llm_provider.generate_structured(
            prompt=DOCTOR_PROMPT,
            schema_model=RiskAssessment,
            context=context
        )
    except Exception:
        result = RiskAssessment(risk_score=0.0, assessment="Error", identified_issues=[])
        
    return {"doctor_output": result}

async def coach_node(state: CouncilState):
    print("--- [Council] Guardian Active ---")
    
    # Inject Memory
    memories = state.get("past_memories", [])
    memory_context = "\n".join([f"- {m.statement} (Outcome: {m.outcome})" for m in memories]) if memories else "None"
    
    context = f"Input: {state['input_data']}\nUser History:\n{memory_context}"
    
    try:
        result = await llm_provider.generate_structured(
            prompt=COACH_PROMPT,
            schema_model=RiskAssessment,
            context=context
        )
    except Exception:
        result = RiskAssessment(risk_score=0.0, assessment="Error", identified_issues=[])
        
    return {"coach_output": result}

async def synthesizer_node(state: CouncilState):
    print("--- [Council] Chair Synthesizing ---")
    
    doctor_res = state.get("doctor_output")
    coach_res = state.get("coach_output")
    memories = state.get("past_memories", [])
    
    context = f"""
    Dr. Nexus Assessment: {doctor_res.assessment if doctor_res else 'None'}
    Risk: {doctor_res.risk_score if doctor_res else 0}
    
    Guardian Assessment: {coach_res.assessment if coach_res else 'None'}
    Risk: {coach_res.risk_score if coach_res else 0}
    
    Past Relevant Episodes:
    {json.dumps([m.statement for m in memories], indent=2) if memories else "None"}
    """
    
    try:
        result = await llm_provider.generate_structured(
            prompt=SYNTHESIZER_PROMPT,
            schema_model=CouncilActionPlan,
            context=context
        )
    except Exception:
        result = CouncilActionPlan(summary="Error", risk_level="UNKNOWN", actions=[])
        
    # Convert Pydantic to Dict for final output compatibility
    return {"final_output": result.model_dump()}

# --- Graph Construction ---
workflow = StateGraph(CouncilState)

workflow.add_node("triage", triage_node)
workflow.add_node("doctor", doctor_node)
workflow.add_node("coach", coach_node)
workflow.add_node("synthesizer", synthesizer_node)

workflow.set_entry_point("triage")

# Conditional Logic
def route_triage(state: CouncilState):
    res = state["triage_result"]
    routes = []
    if res.needs_doctor:
        routes.append("doctor")
    if res.needs_coach:
        routes.append("coach")
    
    # If nothing needed, go straight to end (or synthesizer with empty)
    if not routes:
        return "synthesizer" # Let synthesizer close it out
        
    return routes

workflow.add_conditional_edges(
    "triage",
    route_triage,
    ["doctor", "coach", "synthesizer"]
)

# Both experts go to synthesizer
workflow.add_edge("doctor", "synthesizer")
workflow.add_edge("coach", "synthesizer")
workflow.add_edge("synthesizer", END)

council_graph = workflow.compile()
