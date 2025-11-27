import json
import logging
from typing import Dict, Any, List
from backend.core.llm import llm_provider
from langchain_core.messages import SystemMessage, HumanMessage

logger = logging.getLogger("vital_enricher")

ENRICHMENT_PROMPT = """
You are the Perception Engine of VitalSense.
Your task is to extract structured Knowledge Graph data from the user's memory or input.

Ontology:
- Node Types: 'Activity', 'Symptom', 'Project', 'Entertainment', 'Entity' (generic), 'State' (e.g. Tired).
- Relation Types: 'CAUSES', 'RELATED_TO', 'PART_OF', 'FOLLOWED_BY', 'INTERRUPTS'.

Input Text: "{text}"

Return a JSON object with this structure:
{{
    "nodes": [
        {{ "id": "unique_id_lower_case", "type": "NodeType", "label": "Readable Label" }}
    ],
    "edges": [
        {{ "source": "source_id", "target": "target_id", "relation": "RELATION_TYPE" }}
    ]
}}

Rules:
1. Be granular. "Coding python" -> Activity: "Coding", Entity: "Python".
2. Infer context. "Back hurts" -> Symptom: "Back Pain".
3. Return ONLY JSON.
"""

class GraphEnricher:
    """
    Semantically enriches raw text into structured Graph Data.
    Uses LLM to extract Entities and Relationships.
    """
    
    async def enrich_memory(self, text: str) -> Dict[str, Any]:
        """
        Extracts nodes and edges from text.
        """
        try:
            # Construct Prompt
            prompt = ENRICHMENT_PROMPT.format(text=text)
            
            # Call LLM (using generate_chat for simplicity, or generate_structured if available)
            # We'll use generate_chat and parse JSON for maximum compatibility with current provider
            response = await llm_provider.generate_chat([HumanMessage(content=prompt)])
            
            # Parse JSON
            import re
            json_match = re.search(r"\{.*\}", response, re.DOTALL)
            if json_match:
                data = json.loads(json_match.group(0))
                return data
            else:
                logger.warning(f"[GraphEnricher] No JSON found in response: {response[:50]}...")
                return {"nodes": [], "edges": []}
                
        except Exception as e:
            logger.error(f"[GraphEnricher] Enrichment failed: {e}")
            return {"nodes": [], "edges": []}

# Global Instance
graph_enricher = GraphEnricher()
