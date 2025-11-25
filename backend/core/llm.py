import os
from typing import Type, TypeVar, Any
from pydantic import BaseModel
from google import genai
from google.genai import types

T = TypeVar("T", bound=BaseModel)

class GeminiProvider:
    """
    Wrapper for Google's Gemini API using the official `google-genai` SDK.
    """
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("⚠️ WARNING: GEMINI_API_KEY not found in environment variables.")
        
        self.client = genai.Client(api_key=api_key)
        self.model_name = "gemini-2.5-flash"

    async def generate_structured(self, prompt: str, schema_model: Type[T], context: str = "") -> T:
        """
        Generates a structured response strictly adhering to the Pydantic schema.
        """
        full_prompt = f"{context}\n\nTask: {prompt}"
        
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=full_prompt,
                config={
                    "response_mime_type": "application/json",
                    "response_json_schema": schema_model.model_json_schema(),
                },
            )
            return schema_model.model_validate_json(response.text)
            
        except Exception as e:
            print(f"❌ Gemini API Error: {e}")
            raise e

    async def analyze_image(self, image: Any, prompt: str, schema_model: Type[T]) -> T:
        """
        Multimodal analysis: Image + Prompt -> Structured Output.
        """
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=[image, prompt],
                config={
                    "response_mime_type": "application/json",
                    "response_json_schema": schema_model.model_json_schema(),
                },
            )
            return schema_model.model_validate_json(response.text)
        except Exception as e:
            print(f"❌ Gemini Vision Error: {e}")
            raise e

    async def get_embedding(self, text: str) -> list[float]:
        """
        Generates vector embedding for text using 'text-embedding-004'.
        """
        try:
            result = self.client.models.embed_content(
                model="text-embedding-004",
                contents=text
            )
            return result.embeddings[0].values
        except Exception as e:
            print(f"❌ Gemini Embedding Error: {e}")
            return []

    async def extract_memory_dimensions(self, full_log: str) -> T:
        """
        Extracts structured MemoryEntry from a raw event log.
        """
        # Avoid circular import
        from backend.agents.schemas import MemoryEntry
        
        prompt = """
        Analyze the following health event log.
        Extract structured memory dimensions for the Knowledge Graph.
        
        Log:
        {log}
        
        Return a JSON matching the MemoryEntry schema.
        """.format(log=full_log)
        
        return await self.generate_structured(prompt, MemoryEntry)

# Global Instance
llm_provider = GeminiProvider()
