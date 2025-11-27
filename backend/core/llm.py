import os
from typing import Type, TypeVar, Any
from pydantic import BaseModel
from google import genai
from google.genai import types
from openai import OpenAI
import json

T = TypeVar("T", bound=BaseModel)

class LocalProvider:
    """
    Wrapper for Local LLM (e.g., LM Studio, Ollama) using OpenAI-compatible API.
    Defaults to http://localhost:1234/v1
    """
    def __init__(self):
        self.base_url = os.getenv("LOCAL_LLM_URL", "http://localhost:1234/v1")
        self.api_key = os.getenv("LOCAL_LLM_KEY", "lm-studio")
        
        # Auto-detect model
        try:
            # We use a temporary client to fetch models
            temp_client = OpenAI(base_url=self.base_url, api_key=self.api_key)
            models = temp_client.models.list()
            if models.data:
                self.model_name = models.data[0].id
                print(f"🔌 Auto-detected Local Model: {self.model_name}")
            else:
                self.model_name = os.getenv("LOCAL_LLM_MODEL", "qwen-2.5-7b-instruct")
                print(f"⚠️ No models found via API. Using default: {self.model_name}")
        except Exception as e:
            print(f"⚠️ Failed to auto-detect model: {e}")
            self.model_name = os.getenv("LOCAL_LLM_MODEL", "qwen-2.5-7b-instruct")
        
        print(f"🔌 Connecting to Local LLM at {self.base_url} (Target: {self.model_name})...")
        self.client = OpenAI(base_url=self.base_url, api_key=self.api_key)

    async def generate_structured(self, prompt: str, schema_model: Type[T], context: str = "") -> T:
        """
        Generates structured JSON.
        """
        full_prompt = f"{context}\n\nTask: {prompt}\n\nOutput strictly in JSON format matching this schema:\n{json.dumps(schema_model.model_json_schema())}"
        
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant. Output strictly valid JSON."},
                    {"role": "user", "content": full_prompt}
                ],
                # response_format={"type": "json_object"}, # Not supported by all local models
                temperature=0.2
            )
            content = response.choices[0].message.content
            # Clean up markdown
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].split("```")[0].strip()
                
            return schema_model.model_validate_json(content)
        except Exception as e:
            print(f"❌ Local LLM Error: {e}")
            raise e

    async def analyze_image(self, image: Any, prompt: str, schema_model: Type[T]) -> T:
        """
        Vision capability for Local LLM (e.g., Qwen-VL).
        Accepts PIL Image, converts to base64, and sends to API.
        """
        import base64
        import io
        from PIL import Image

        # 1. Convert PIL Image to Base64
        try:
            if isinstance(image, Image.Image):
                buffered = io.BytesIO()
                # Convert to RGB if necessary (e.g. RGBA)
                if image.mode in ('RGBA', 'LA'):
                    background = Image.new(image.mode[:-1], image.size, (255, 255, 255))
                    background.paste(image, image.split()[-1])
                    image = background
                elif image.mode != 'RGB':
                    image = image.convert('RGB')
                    
                image.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
                img_url = f"data:image/jpeg;base64,{img_str}"
            else:
                print("⚠️ Local Vision: Unsupported image type. Expected PIL Image.")
                return schema_model() # Return empty model to avoid crash, but validation will fail if fields required
        except Exception as e:
             print(f"❌ Local Vision Image Processing Error: {e}")
             raise e

        # 2. Construct Payload
        full_prompt = f"Task: {prompt}\n\nOutput strictly in JSON format matching this schema:\n{json.dumps(schema_model.model_json_schema())}"
        
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": full_prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": img_url
                                }
                            }
                        ]
                    }
                ],
                max_tokens=1024,
                temperature=0.2
            )
            
            # 3. Parse Response
            content = response.choices[0].message.content
            # Clean up markdown code blocks if present
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].split("```")[0].strip()
                
            return schema_model.model_validate_json(content)
            
        except Exception as e:
            print(f"❌ Local Vision API Error: {e}")
            # Return a safe default if possible, or re-raise
            # For ScreenAnalysis, we can try to return a dummy object to keep the loop running
            # But strictly, we should raise or return a valid empty object if fields are optional.
            # Since fields are required, we must raise or construct a valid dummy.
            print("Returning dummy ScreenAnalysis due to error.")
            # We can't easily construct a generic dummy for T, so we raise.
            raise e

    async def get_embedding(self, text: str) -> list[float]:
        try:
            response = self.client.embeddings.create(
                model="text-embedding-nomic-embed-text-v1.5", # Common local embedding model
                input=text
            )
            return response.data[0].embedding
        except Exception as e:
            print(f"❌ Local Embedding Error: {e}")
            return []

    async def generate_chat(self, messages: list[Any]) -> str:
        formatted_msgs = []
        for msg in messages:
            role = "user"
            if msg.type == "system": role = "system"
            elif msg.type == "ai": role = "assistant"
            formatted_msgs.append({"role": role, "content": msg.content})
            
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=formatted_msgs,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"❌ Local Chat Error: {e}")
            return "I'm offline."

    async def summarize_day(self, context: str) -> str:
        prompt = f"Summarize these logs into a narrative:\n{context}"
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return "Summary failed."

    async def extract_memory_dimensions(self, full_log: str) -> T:
        # Avoid circular import
        from backend.agents.schemas import MemoryEntry
        prompt = f"Analyze log and extract MemoryEntry JSON:\n{full_log}"
        return await self.generate_structured(prompt, MemoryEntry)


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
provider_type = os.getenv("LLM_PROVIDER", "gemini").lower()
if provider_type == "local":
    llm_provider = LocalProvider()
else:
    llm_provider = GeminiProvider()
