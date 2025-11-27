import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.core.risk_engine import risk_engine

def test_risk_override():
    print("--- Testing Risk Override ---")
    
    # 1. Baseline: High Duration Risk
    print("\n1. Baseline Check (No Override)")
    result = risk_engine.calculate_deterministic_risk("coding", duration_minutes=400)
    print(f"Risk Score: {result['score']}")
    print(f"Reasoning: {result['reasoning']}")
    
    if result['score'] < 0.4:
        print("FAIL: Expected high risk for 400m duration.")
        return

    # 2. Set Override
    print("\n2. Setting Override for 'duration'")
    risk_engine.set_override("duration", 60) # 1 hour override
    
    # 3. Check with Override
    print("\n3. Check with Override Active")
    result_override = risk_engine.calculate_deterministic_risk("coding", duration_minutes=400)
    print(f"Risk Score: {result_override['score']}")
    print(f"Reasoning: {result_override['reasoning']}")
    
    if result_override['score'] > 0.0:
        print("FAIL: Expected 0.0 risk with override active.")
        return
        
    # 4. Check other risks still work
    print("\n4. Check other risks (Symptoms) still work")
    result_mixed = risk_engine.calculate_deterministic_risk("chest pain", duration_minutes=400)
    print(f"Risk Score: {result_mixed['score']}")
    print(f"Reasoning: {result_mixed['reasoning']}")
    
    if result_mixed['score'] < 0.5:
        print("FAIL: Expected symptom risk to persist.")
        return

    print("\nSUCCESS: Risk Override Logic Verified.")

if __name__ == "__main__":
    test_risk_override()
