import re

def calculate_deterministic_risk(text: str, duration_minutes: int = 0) -> dict:
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
    for word in neglect:
        if word in text_lower:
            score += 0.2
            reasons.append(f"Neglect keyword: '{word}' (+0.2)")
            break

    # 3. Duration Multipliers
    # Only apply if there are symptoms or neglect, OR if duration is extreme
    if duration_minutes > 0:
        if duration_minutes > 360: # 6 hours
            score += 0.4
            reasons.append(f"Extreme duration (>6h): {duration_minutes}m (+0.4)")
        elif duration_minutes > 240: # 4 hours
            score += 0.3
            reasons.append(f"High duration (>4h): {duration_minutes}m (+0.3)")
        elif duration_minutes > 120: # 2 hours
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
