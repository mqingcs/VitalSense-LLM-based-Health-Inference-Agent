import re
from typing import Dict, Any, List
from backend.core.graph_service import graph_service
from backend.agents.schemas import RiskAssessment, MemoryEntry

from backend.core.profile_service import profile_service

class RiskEngine:
    """
    Hybrid Risk Assessment Engine.
    Combines fast deterministic checks with deep GraphRAG pattern detection.
    """
    
    def __init__(self):
        self.overrides: Dict[str, float] = {} # key: risk_type, value: expiration_timestamp

    def set_override(self, risk_type: str, duration_minutes: int):
        """
        Sets an override for a specific risk type.
        """
        import time
        expiration = time.time() + (duration_minutes * 60)
        self.overrides[risk_type] = expiration
        print(f"[RiskEngine] Override set for '{risk_type}' until {expiration}")

    def adjust_tolerance(self, risk_type: str, amount: float):
        """
        Feedback Loop: Adjusts the user's tolerance for a specific risk.
        Called when user dismisses a card.
        """
        # For now, we implement this by updating the Profile's risk modifier
        # This creates a permanent adaptation
        current_mod = profile_service.get_risk_modifier(risk_type)
        # If user dismisses, they want LESS sensitivity, so we DECREASE the modifier
        # (Wait, logic check: Modifier multiplies duration. Lower modifier = Lower effective duration = Less Risk)
        # So yes, we decrease the modifier.
        
        new_mod = max(0.5, current_mod - amount) # Don't go below 0.5
        profile_service.profile.risk_modifiers[risk_type] = new_mod
        profile_service._save_profile()
        print(f"[RiskEngine] Tolerance Adjusted: {risk_type} modifier -> {new_mod}")

    def _is_overridden(self, risk_type: str) -> bool:
        """Checks if a risk type is currently overridden."""
        import time
        if risk_type in self.overrides:
            if time.time() < self.overrides[risk_type]:
                return True
            else:
                del self.overrides[risk_type] # Expired
        return False

    def calculate_deterministic_risk(self, text: str, duration_minutes: int = 0) -> dict:
        """
        Calculates a deterministic risk score (0.0 - 1.0) based on keywords and duration.
        Returns score and reasoning.
        """
        score = 0.0
        reasons = []
        text_lower = text.lower()

        # 1. Symptom Keywords
        high_severity = ["faint", "collapse", "chest pain", "severe", "agony", "unbearable", "crushing"]
        medium_severity = ["headache", "pain", "dizzy", "blur", "strain", "tired", "exhausted", "migraine", "throbbing"]
        
        if not self._is_overridden("symptoms"):
            for word in high_severity:
                if word in text_lower:
                    score += 0.5
                    reasons.append(f"High severity keyword: '{word}' (+0.5)")
                    break # Count max one high severity trigger to avoid stacking too fast
                    
            for word in medium_severity:
                if word in text_lower:
                    score += 0.3
                    reasons.append(f"Medium severity keyword: '{word}' (+0.3)")
                    break

        # 2. Neglect Keywords
        neglect = ["without water", "no water", "dehydrated", "skipped meal", "no food", "starving", "haven't eaten"]
        if not self._is_overridden("neglect"):
            for word in neglect:
                if word in text_lower:
                    score += 0.2
                    reasons.append(f"Neglect keyword: '{word}' (+0.2)")
                    break

        # 3. Duration Multipliers (Simple)
        # "duration" override blocks all duration-based risks (e.g. "I'm working late")
        if duration_minutes > 0 and not self._is_overridden("duration"):
            # Apply Dynamic Modifier from Profile
            modifier = profile_service.get_risk_modifier("sedentary")
            effective_duration = duration_minutes * modifier
            
            if modifier > 1.0:
                 reasons.append(f"Risk Modifier Active: Sedentary x{modifier}")

            if effective_duration > 360: # 6 hours
                score += 0.4
                reasons.append(f"Extreme duration (>6h): {duration_minutes}m (+0.4)")
            elif effective_duration > 240: # 4 hours
                score += 0.3
                reasons.append(f"High duration (>4h): {duration_minutes}m (+0.3)")
            elif effective_duration > 120: # 2 hours
                if score > 0: # Only aggravate existing issues
                    score += 0.1
                    reasons.append(f"Moderate duration (>2h): {duration_minutes}m (+0.1)")

        # Cap at 1.0
        score = min(score, 1.0)
        
        # Determine Level
        level = "LOW"
        if score >= 0.7:
            level = "HIGH"
        elif score >= 0.4:
            level = "MEDIUM"

        return {
            "score": round(score, 2),
            "level": level,
            "reasoning": "; ".join(reasons)
        }

    def assess_complex_risks(self, current_memories: List[MemoryEntry]) -> Dict[str, Any]:
        """
        Uses GraphRAG to detect complex temporal patterns.
        """
        # 1. Rebuild Graph with recent context
        graph_service.build_graph(current_memories)
        
        risks = []
        total_risk_score = 0.0
        all_involved_nodes = set()
        
        # 2. Check "The Grind" (Work > 1h without break)
        grind = graph_service.detect_grind_pattern(threshold_minutes=60)
        if grind["detected"]:
            # Apply Modifier
            modifier = profile_service.get_risk_modifier("sedentary")
            
            risks.append(f"GRAPH_ALERT: {grind['reason']} (Modifier: x{modifier})")
            total_risk_score += (0.4 * modifier) # Significant risk factor scaled
            
            if "involved_nodes" in grind:
                all_involved_nodes.update(grind["involved_nodes"])
            
        # 3. Check "Mixed Media" (Work -> Ent)
        mixed = graph_service.detect_mixed_media_pattern()
        if mixed["detected"]:
            # Apply Modifier
            modifier = profile_service.get_risk_modifier("screen_time")
            
            risks.append(f"GRAPH_ALERT: {mixed['reason']} (Modifier: x{modifier})")
            total_risk_score += (0.2 * modifier) # Moderate risk scaled
            
            if "involved_nodes" in mixed:
                all_involved_nodes.update(mixed["involved_nodes"])
            
        return {
            "graph_score": min(total_risk_score, 1.0),
            "graph_reasons": risks,
            "involved_nodes": list(all_involved_nodes)
        }

# Global Instance
risk_engine = RiskEngine()
