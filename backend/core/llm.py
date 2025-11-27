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

    async def generate_chat(self, messages: list[Any]) -> str:
        """
        Generates a chat response.
        Args:
            messages: List of LangChain message objects (SystemMessage, HumanMessage, AIMessage).
        """
        # Convert LangChain messages to Gemini format
        gemini_messages = []
        system_instruction = None
        
        for msg in messages:
            if msg.type == "system":
                system_instruction = msg.content
            elif msg.type == "human":
                gemini_messages.append(types.Content(role="user", parts=[types.Part.from_text(text=msg.content)]))
            elif msg.type == "ai":
                gemini_messages.append(types.Content(role="model", parts=[types.Part.from_text(text=msg.content)]))
                
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=gemini_messages,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction
                )
            )
            return response.text if response.text else ""
        except Exception as e:
            print(f"❌ Gemini Chat Error: {e}")
            return "I'm having trouble connecting to my thought process right now."
    async def summarize_day(self, context: str) -> str:
        """
        Summarizes a list of raw memory logs into a cohesive narrative.
        """
        prompt = f"""
        You are the 'Hippocampus' of an AI agent.
        Your task is to consolidate the following raw memory logs into a single, cohesive narrative summary.
        
        Rules:
        1. Ignore repetitive noise (e.g., 50 logs of "typing").
        2. Focus on the 'Story': What did the user work on? How did they feel? What were the outcomes?
        3. Be concise but comprehensive.
        
        Raw Logs:
        {context}
        
        Summary:
        """
        
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            return response.text if response.text else "No significant events."
        except Exception as e:
            print(f"❌ Gemini Summary Error: {e}")
            return "Failed to generate summary."
# Global Instance
llm_provider = GeminiProvider()
