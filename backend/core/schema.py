from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime

class HealthMetric(BaseModel):
    name: str
    value: float
    unit: str
    timestamp: datetime = Field(default_factory=datetime.now)

class UserHealthProfile(BaseModel):
    """
    The 'Digital Twin' State.
    """
    user_id: str
    physical_status: Dict[str, float] = Field(default_factory=dict) # e.g. {"fatigue": 0.8}
    mental_status: Dict[str, float] = Field(default_factory=dict)   # e.g. {"stress": 0.9}
    recent_activities: List[str] = Field(default_factory=list)
    last_updated: datetime = Field(default_factory=datetime.now)

class AnalysisResult(BaseModel):
    """
    Output from the Agent Council.
    """
    risk_level: str # LOW, MEDIUM, HIGH
    summary: str
    recommended_actions: List[str]
    council_debate_log: List[str] # For transparency
