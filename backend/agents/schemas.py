from pydantic import BaseModel, Field
from typing import List, Optional

class TriageResult(BaseModel):
    """
    Output schema for the Triage Agent.
    """
    needs_doctor: bool = Field(description="True if medical/physical symptoms are detected.")
    needs_coach: bool = Field(description="True if lifestyle/habit issues are detected.")
    reasoning: str = Field(description="Brief explanation of the routing decision.")

class RiskAssessment(BaseModel):
    """
    Output schema for Dr. Nexus and Guardian.
    """
    risk_score: float = Field(description="Risk level from 0.0 (Safe) to 1.0 (Critical).")
    assessment: str = Field(description="Detailed analysis of the user's condition.")
    identified_issues: List[str] = Field(description="List of specific issues found (e.g. 'Sleep Deprivation').")

class CouncilActionPlan(BaseModel):
    """
    Output schema for the Council Chair (Synthesizer).
    """
    summary: str = Field(description="Executive summary of the user's health state.")
    risk_level: str = Field(description="Overall risk level: LOW, MEDIUM, or HIGH.")
    risk_type: str = Field(description="The primary category of the risk (e.g., 'sedentary', 'posture', 'stress', 'fatigue').", default="sedentary")
    actions: List[str] = Field(description="Concrete, actionable steps for the user to take.")
    graph_highlights: List[str] = Field(description="List of Memory IDs that contributed to the risk assessment.", default=[])

class MemoryEntry(BaseModel):
    """
    Structured memory for GraphRAG.
    """
    timestamp: str = Field(description="ISO 8601 timestamp of the event.")
    scene: str = Field(description="Contextual scene (e.g., 'Late night coding').")
    statement: str = Field(description="The core event or signal detected.")
    entities: List[str] = Field(description="Key entities extracted (e.g., ['Insomnia', 'Heart Rate']).")
    user_state: str = Field(description="Inferred emotional or physical state (e.g., 'Anxious').")
    outcome: str = Field(description="The action taken or advice given.")
    remarks: Optional[str] = Field(description="Meta-analysis or additional notes.", default=None)
    id: Optional[str] = Field(description="Unique ID of the memory record.", default=None)

