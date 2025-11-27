import asyncio
import os
from PIL import Image
from pydantic import BaseModel, Field
from backend.core.llm import LocalProvider

# Define a simple schema for testing
class ImageDescription(BaseModel):
    color: str = Field(description="The dominant color of the image.")
    shape: str = Field(description="The shape shown in the image.")

async def test_vision():
    # 1. Setup Provider
    # Ensure env vars are set (mocking them if needed, but assuming user set them)
    os.environ["LOCAL_LLM_URL"] = "http://localhost:1234/v1"
    os.environ["LOCAL_LLM_MODEL"] = "qwen-2.5-7b-instruct" # Or whatever is loaded
    
    provider = LocalProvider()
    
    # 2. Create Dummy Image (Red Square)
    img = Image.new('RGB', (100, 100), color = 'red')
    
    print("--- Testing Local Vision ---")
    print("Sending Red Square Image...")
    
    try:
        result = await provider.analyze_image(
            image=img,
            prompt="What color and shape is this?",
            schema_model=ImageDescription
        )
        print("\n--- Result ---")
        print(result)
        
        if "red" in result.color.lower():
            print("SUCCESS: Color detected correctly.")
        else:
            print(f"FAILURE: Unexpected color {result.color}")
            
    except Exception as e:
        print(f"\nFAILURE: {e}")

if __name__ == "__main__":
    asyncio.run(test_vision())
