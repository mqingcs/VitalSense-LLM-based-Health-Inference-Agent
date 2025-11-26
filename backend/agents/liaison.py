from typing import Dict, Any, List
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.tools import tool

from backend.core.llm import llm_provider
from backend.core.profile_service import profile_service
from backend.core.memory import hippocampus
from backend.core.graph_service import graph_service
from backend.agents.personas import LIAISON_PROMPT

# --- Tools ---

@tool
def update_profile(key: str, value: str, action: str = "add"):
    """
    Updates the user's profile.
    Args:
        key: 'trait', 'condition', or 'habit'.
        value: The value to add/remove (e.g., 'Back Pain').
        action: 'add' or 'remove'.
    """
    if key == "trait":
        profile_service.update_trait(value, action)
    elif key == "condition":
        profile_service.update_condition(value, action)
    elif key == "habit":
        # Habits are stored in traits list for now in ProfileService, let's fix that or map it
        # ProfileService has habits list but update_trait/condition methods. 
        # Let's assume we add a update_habit method or map it.
        # Checking ProfileService... it has habits field but no update_habit method in the snippet I wrote.
        # I will assume I need to add it or use a generic update.
        # For now, let's just use traits for habits or add it dynamically.
        # Actually, let's implement it properly in ProfileService later or patch it here.
        # Patching:
        if action == "add" and value not in profile_service.profile.habits:
            profile_service.profile.habits.append(value)
        elif action == "remove" and value in profile_service.profile.habits:
            profile_service.profile.habits.remove(value)
        profile_service._save_profile()
        
    return f"Profile updated: {action} {key} '{value}'."

@tool
def manage_memory(action: str, query: str):
    """
    Manages user memories.
    Args:
        action: 'delete' or 'search'.
        query: The content to search for or delete.
    """
    # This is a simplified version. Real deletion needs ID.
    # We'll search first then delete if action is delete.
    # For now, just searching.
    return "Memory management is complex. Please use the Memory Manager UI for precise deletion."

@tool
def set_preference(key: str, value: str):
    """
    Sets a system preference.
    Args:
        key: e.g., 'mute_alerts'.
        value: 'true' or 'false'.
    """
    val = value.lower() == "true"
    profile_service.set_preference(key, val)
    return f"Preference set: {key} = {val}"

@tool
def query_graph(question: str):
    """
    Queries the knowledge graph for insights.
    Args:
        question: The user's question about their behavior.
    """
    # Simple heuristic for now
    if "work" in question.lower():
        grind = graph_service.detect_grind_pattern()
        return f"Graph Analysis: Grind detected? {grind['detected']}. Duration: {grind['duration']}m."
    return "Graph query not fully implemented yet."

tools = [update_profile, manage_memory, set_preference, query_graph]

# --- Agent ---

class LiaisonState(Dict):
    messages: List[Any]
    user_profile: str

async def liaison_node(state: LiaisonState):
    print("--- [Liaison] Thinking ---")
    
    # 1. Get Profile Context
    profile_str = profile_service.get_context_str()
    
    # 2. Construct Prompt
    system_msg = SystemMessage(content=LIAISON_PROMPT.format(user_profile=profile_str))
    messages = [system_msg] + state["messages"]
    
    # 3. ReAct Loop
    max_turns = 3
    current_messages = messages.copy()
    
    for _ in range(max_turns):
        # Call LLM
        response_text = await llm_provider.generate_chat(current_messages)
        
        # Check for Tool Call (JSON block)
        import re
        import json
        
        tool_match = re.search(r"```json\s*(\{.*?\})\s*```", response_text, re.DOTALL)
        
        if tool_match:
            try:
                tool_data = json.loads(tool_match.group(1))
                tool_name = tool_data.get("tool")
                tool_args = tool_data.get("args", {})
                
                print(f"--- [Liaison] Executing Tool: {tool_name} with {tool_args} ---")
                
                # Execute Tool
                tool_result = "Error: Tool not found."
                if tool_name == "update_profile":
                    tool_result = update_profile.invoke(tool_args)
                elif tool_name == "manage_memory":
                    tool_result = manage_memory.invoke(tool_args)
                elif tool_name == "set_preference":
                    tool_result = set_preference.invoke(tool_args)
                elif tool_name == "query_graph":
                    tool_result = query_graph.invoke(tool_args)
                
                print(f"--- [Liaison] Tool Result: {tool_result} ---")
                
                # Append to history and loop again
                current_messages.append(AIMessage(content=response_text))
                current_messages.append(HumanMessage(content=f"Tool Output: {tool_result}"))
                
            except Exception as e:
                print(f"--- [Liaison] Tool Execution Error: {e} ---")
                current_messages.append(AIMessage(content=response_text))
                current_messages.append(HumanMessage(content=f"Tool Execution Error: {e}"))
        else:
            # No tool call, just return the response
            return {"messages": [AIMessage(content=response_text)]}
            
    return {"messages": [AIMessage(content="I'm thinking too much. Let's pause.")]}

# --- Workflow ---

workflow = StateGraph(LiaisonState)
workflow.add_node("liaison", liaison_node)
workflow.set_entry_point("liaison")
workflow.add_edge("liaison", END)

liaison_agent = workflow.compile()
