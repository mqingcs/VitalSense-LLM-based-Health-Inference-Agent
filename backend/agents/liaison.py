from typing import Dict, Any, List
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.tools import tool

from backend.core.llm import llm_provider
from backend.core.profile_service import profile_service
from backend.core.memory import hippocampus
from backend.core.graph_service import graph_service
from backend.core.risk_engine import risk_engine
from backend.agents.personas import LIAISON_PROMPT

# --- Tools ---

@tool
def update_profile(key: str, value: str, action: str = "add"):
    """
    Updates the user's persistent profile.
    Args:
        key: 'trait', 'habit', 'preference', or 'condition'.
        value: The value to add/remove (e.g., 'Night Owl', 'Back Pain').
        action: 'add' or 'remove'.
    """
    if key == "trait":
        profile_service.update_trait(value, action)
    elif key == "habit":
        # Simplified for prototype
        if action == "add": profile_service.profile.habits.append(value)
        elif action == "remove" and value in profile_service.profile.habits: profile_service.profile.habits.remove(value)
        profile_service._save_profile()
    elif key == "condition":
        profile_service.update_condition(value, action)
    elif key == "preference":
        profile_service.set_preference(value, True if action == "add" else False) # Simplified
        
    return f"Profile Updated: {action.upper()} {key} -> {value}"

@tool
async def manage_memory(action: str, query: str):
    """
    Manages user memories.
    Args:
        action: 'delete' or 'search'.
        query: The content to search for or delete.
    """
    if action == "search":
        memories = await hippocampus.recall(query)
        if not memories:
            return "Memory Search: No relevant memories found."
        
        summary = "Memory Search Results:\n"
        for m in memories:
            summary += f"- [{m.timestamp}] {m.statement}\n"
        return summary
        
    return "Memory management: Deletion requires specific ID. Please use the Memory Manager UI."

# ... (other tools remain sync) ...



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
async def query_graph(question: str):
    """
    Queries the knowledge graph for insights.
    Args:
        question: The user's question about their behavior.
    """
    # "Smart Query" Strategy:
    # Instead of guessing intent with keywords, we provide a rich context 
    # combining recent timeline (structure) and semantic search (content).
    
    # 1. Get Timeline Context (Structure & Duration)
    activities = graph_service.get_recent_activity(limit=15)
    timeline_str = "Recent Timeline:\n"
    if activities:
        for act in activities:
            timeline_str += f"- [{act['timestamp']}] {act['statement']} (Duration: {act['duration']})\n"
    else:
        timeline_str += "No recent activity recorded.\n"

    # 2. Semantic Search (Content)
    # We search for the specific question to find relevant past episodes
    memories = await hippocampus.recall(question, k=5)
    memory_str = "Relevant Memories:\n"
    if memories:
        for m in memories:
            memory_str += f"- [{m.timestamp}] {m.statement}\n"
    else:
        memory_str += "No specific memories found for this query.\n"
        
    # 3. Grind Detection (Specific Pattern)
    # We always run this as a background check for context
    grind = graph_service.detect_grind_pattern()
    grind_str = f"Grind Pattern Detected: {grind['detected']} (Duration: {grind['duration']}m)\n"
    
    return f"Graph Analysis Results:\n\n{timeline_str}\n{memory_str}\n{grind_str}"



@tool
def set_risk_override(risk_type: str, duration_hours: int, reason: str):
    """
    Overrides (suppresses) a specific risk factor for a set duration.
    Use this when the user explicitly wants to ignore a risk (e.g., "I'm staying up late").
    Args:
        risk_type: 'duration' (for time/work limits), 'symptoms', or 'neglect'.
        duration_hours: How long to suppress this risk (in hours).
        reason: Why the override is being set.
    """
    risk_engine.set_override(risk_type, duration_hours * 60)
    return f"Risk Override Set: Suppressing '{risk_type}' for {duration_hours} hours. Reason: {reason}"

@tool
def fetch_profile_context(category: str):
    """
    Fetches specific details from the user's profile.
    Args:
        category: 'traits', 'conditions', 'habits', 'preferences', or 'summary'.
    """
    if category == "summary":
        return profile_service.get_context_str()
    
    # Access internal profile object directly for granular access
    # (In a real system, ProfileService would have granular getters)
    p = profile_service.profile
    if category == "traits":
        return f"Traits: {p.traits}"
    elif category == "conditions":
        return f"Conditions: {p.conditions}"
    elif category == "habits":
        return f"Habits: {p.habits}"
    elif category == "preferences":
        return f"Preferences: {p.preferences}"
        
    return "Unknown category. Available: traits, conditions, habits, preferences, summary."

tools = [update_profile, manage_memory, set_preference, query_graph, set_risk_override, fetch_profile_context]

# --- Agent ---

class LiaisonState(Dict):
    messages: List[Any]
    user_profile: str

async def liaison_node(state: LiaisonState):
    print("--- [Liaison] Thinking ---")
    
    # 1. Get Profile Summary
    profile_summary = f"User: {profile_service.profile.name}. Role: {profile_service.profile.role}."
    
    # 2. Construct Prompt
    autonomy_instruction = """
    CRITICAL INSTRUCTION: You are an AUTONOMOUS AGENT.
    1. **On-Demand Memory**: You do NOT have the full user profile loaded. If you need to know about allergies, habits, or preferences to answer a question, use `fetch_profile_context`.
    2. **Proactivity**: If you see a risk, act on it.
    3. **Dynamic Modeling**: If the user mentions a physical ailment (e.g., "My back hurts"), you MUST use `update_profile(key='condition', value='Back Pain', action='add')` immediately. This adjusts the risk engine.
    4. **Task Chaining**: Combine tools to solve problems.
    """
    
    system_msg = SystemMessage(content=LIAISON_PROMPT.format(user_profile=profile_summary) + "\n\n" + autonomy_instruction)
    messages = [system_msg] + state["messages"]
    
    # 3. ReAct Loop
    max_turns = 5
    current_messages = messages.copy()
    new_messages = [] # Track messages generated in this node
    
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
                    tool_result = await manage_memory.ainvoke(tool_args)
                elif tool_name == "set_preference":
                    tool_result = set_preference.invoke(tool_args)
                elif tool_name == "query_graph":
                    tool_result = await query_graph.ainvoke(tool_args)
                elif tool_name == "set_risk_override":
                    tool_result = set_risk_override.invoke(tool_args)
                elif tool_name == "fetch_profile_context":
                    tool_result = fetch_profile_context.invoke(tool_args)
                
                print(f"--- [Liaison] Tool Result: {tool_result} ---")
                
                # Append to history
                ai_msg = AIMessage(content=response_text)
                tool_msg = HumanMessage(content=f"Tool Output: {tool_result}")
                
                current_messages.append(ai_msg)
                current_messages.append(tool_msg)
                
                new_messages.append(ai_msg)
                new_messages.append(tool_msg)
                
            except Exception as e:
                print(f"--- [Liaison] Tool Execution Error: {e} ---")
                ai_msg = AIMessage(content=response_text)
                err_msg = HumanMessage(content=f"Tool Execution Error: {e}")
                
                current_messages.append(ai_msg)
                current_messages.append(err_msg)
                
                new_messages.append(ai_msg)
                new_messages.append(err_msg)
        else:
            # No tool call, just return the response
            final_msg = AIMessage(content=response_text)
            new_messages.append(final_msg)
            return {"messages": new_messages}
            
    return {"messages": new_messages + [AIMessage(content="I've done a lot of thinking. Let's pause.")]}

# --- Workflow ---

workflow = StateGraph(LiaisonState)
workflow.add_node("liaison", liaison_node)
workflow.set_entry_point("liaison")
workflow.add_edge("liaison", END)

liaison_agent = workflow.compile()
