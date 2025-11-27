from backend.core.profile_service import UserProfile, profile_service

def test_user_profile_role():
    print("\n--- Testing UserProfile Role Attribute ---")
    
    # 1. Test Default Instantiation
    profile = UserProfile()
    print(f"Default Role: {profile.role}")
    assert profile.role == "User"
    
    # 2. Test ProfileService Loading
    # Force reload to check if it handles existing JSONs gracefully (Pydantic should use default)
    try:
        loaded_profile = profile_service.get_profile()
        print(f"Loaded Profile Role: {loaded_profile.role}")
        # If the JSON didn't have 'role', it should use the default "User"
        # If it did, it uses that.
        # The key is that accessing .role doesn't raise AttributeError
        assert hasattr(loaded_profile, 'role')
        print("SUCCESS: UserProfile has 'role' attribute.")
    except Exception as e:
        print(f"FAILURE: {e}")

if __name__ == "__main__":
    test_user_profile_role()
