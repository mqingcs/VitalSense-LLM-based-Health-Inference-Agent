import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.core.profile_service import profile_service
from backend.core.risk_engine import risk_engine

def test_dynamic_modeling():
    print("\n--- Testing Dynamic User Modeling & Adaptive Risk ---")
    
    # 1. Baseline Risk (Sedentary 5 hours)
    # Default modifier is 1.0. 5h = 300m.
    # 300m > 240m (4h) -> Score +0.3
    print("\n1. Baseline Check (No Conditions)")
    # Reset for test
    if "Back Pain" in profile_service.profile.conditions:
        profile_service.update_condition("Back Pain", "remove")
        
    result = risk_engine.calculate_deterministic_risk("coding", duration_minutes=300)
    print(f"Baseline Score: {result['score']}")
    print(f"Reasoning: {result['reasoning']}")
    
    if result['score'] > 0.4:
        print("FAIL: Baseline score unexpectedly high.")
        return

    # 2. Add Condition (Back Pain)
    print("\n2. Adding Condition: 'Back Pain'")
    profile_service.update_condition("Back Pain", "add")
    
    # Verify Modifier
    mod = profile_service.get_risk_modifier("sedentary")
    print(f"Sedentary Modifier: {mod}")
    if mod != 1.5:
        print(f"FAIL: Modifier not updated. Expected 1.5, got {mod}")
        return

    # 3. Check Adaptive Risk
    # Now 300m * 1.5 = 450m.
    # 450m > 360m (6h) -> Score +0.4 (Extreme Duration)
    print("\n3. Check with Condition Active")
    result_adaptive = risk_engine.calculate_deterministic_risk("coding", duration_minutes=300)
    print(f"Adaptive Score: {result_adaptive['score']}")
    print(f"Reasoning: {result_adaptive['reasoning']}")
    
    if result_adaptive['score'] <= result['score']:
        print("FAIL: Risk score did not increase with condition.")
        return
        
    if "Risk Modifier Active" not in result_adaptive['reasoning']:
        print("FAIL: Reasoning missing modifier info.")
        return

    # 4. Cleanup
    print("\n4. Cleanup")
    profile_service.update_condition("Back Pain", "remove")
    mod_reset = profile_service.get_risk_modifier("sedentary")
    if mod_reset != 1.0:
        print("FAIL: Modifier not reset.")
        return

    print("\nSUCCESS: Dynamic Modeling Verified.")

if __name__ == "__main__":
    test_dynamic_modeling()
