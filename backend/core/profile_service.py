import os
import json
from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field

class UserProfile(BaseModel):
    """
    Distinct from episodic memory, this holds the user's long-term traits and conditions.
    """
    name: str = "User"
    role: str = Field(default="User", description="The user's primary role or occupation (e.g., 'Software Engineer').")
    traits: List[str] = Field(default_factory=list, description="Personality or behavioral traits (e.g., 'Programmer', 'Night Owl').")
    conditions: List[str] = Field(default_factory=list, description="Medical or physical conditions (e.g., 'Lumbar Disc Herniation').")
    habits: List[str] = Field(default_factory=list, description="Recurring behaviors (e.g., 'Drinks coffee at 9 AM').")
    preferences: Dict[str, Any] = Field(default_factory=dict, description="System preferences (e.g., 'mute_late_night_alerts': True).")
    risk_modifiers: Dict[str, float] = Field(default_factory=dict, description="Dynamic multipliers for risk categories (e.g., 'sedentary': 1.5).")

class ProfileService:
    """
    Manages the persistent User Profile.
    """
    def __init__(self, storage_path="backend/data/user_profile.json"):
        self.storage_path = storage_path
        self._ensure_storage()
        self.profile = self._load_profile()

    def _ensure_storage(self):
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        if not os.path.exists(self.storage_path):
            default_profile = UserProfile()
            with open(self.storage_path, "w") as f:
                f.write(default_profile.model_dump_json(indent=2))

    def _load_profile(self) -> UserProfile:
        try:
            with open(self.storage_path, "r") as f:
                data = json.load(f)
                return UserProfile(**data)
        except Exception as e:
            print(f"[ProfileService] Error loading profile: {e}")
            return UserProfile()

    def _save_profile(self):
        with open(self.storage_path, "w") as f:
            f.write(self.profile.model_dump_json(indent=2))

    def get_profile(self) -> UserProfile:
        return self.profile

    def update_trait(self, trait: str, action: str = "add"):
        if action == "add" and trait not in self.profile.traits:
            self.profile.traits.append(trait)
        elif action == "remove" and trait in self.profile.traits:
            self.profile.traits.remove(trait)
        self._save_profile()

    def update_condition(self, condition: str, action: str = "add"):
        """
        Updates medical conditions and automatically adjusts risk modifiers.
        """
        condition_lower = condition.lower()
        if action == "add" and condition not in self.profile.conditions:
            self.profile.conditions.append(condition)
            
            # Intelligent Modifier Adjustment
            if "back" in condition_lower or "spine" in condition_lower or "herniation" in condition_lower:
                self.profile.risk_modifiers["sedentary"] = 1.5
                print(f"[ProfileService] Condition '{condition}' added. Sedentary risk increased to 1.5x.")
            elif "eye" in condition_lower or "vision" in condition_lower:
                self.profile.risk_modifiers["screen_time"] = 1.3
                print(f"[ProfileService] Condition '{condition}' added. Screen Time risk increased to 1.3x.")

        elif action == "remove" and condition in self.profile.conditions:
            self.profile.conditions.remove(condition)
            
            # Reset Modifiers if no relevant conditions remain
            # (Simplified logic: if removing back pain, reset sedentary)
            if "back" in condition_lower or "spine" in condition_lower:
                self.profile.risk_modifiers["sedentary"] = 1.0
                print(f"[ProfileService] Condition '{condition}' removed. Sedentary risk reset.")
            elif "eye" in condition_lower:
                self.profile.risk_modifiers["screen_time"] = 1.0

        self._save_profile()

    def get_risk_modifier(self, risk_type: str) -> float:
        """Returns the multiplier for a given risk type (default 1.0)."""
        return self.profile.risk_modifiers.get(risk_type, 1.0)

    def set_preference(self, key: str, value: Any):
        self.profile.preferences[key] = value
        self._save_profile()

    def get_context_str(self) -> str:
        """
        Returns a formatted string for LLM context.
        """
        return f"""
        User Profile:
        - Name: {self.profile.name}
        - Traits: {', '.join(self.profile.traits)}
        - Conditions: {', '.join(self.profile.conditions)}
        - Habits: {', '.join(self.profile.habits)}
        - Risk Modifiers: {json.dumps(self.profile.risk_modifiers)}
        - Preferences: {json.dumps(self.profile.preferences)}
        """

# Global Instance
profile_service = ProfileService()
