import asyncio
from unittest.mock import MagicMock, AsyncMock
from backend.agents.liaison import liaison_agent
from langchain_core.messages import HumanMessage
from backend.core.profile_service import profile_service
from backend.core.graph_service import graph_service
from backend.core.memory import hippocampus

async def test_autonomy():
    print("\n--- Testing Agent Autonomy & Intelligence ---")
    
    # Mock Services to avoid real DB/LLM calls for this logic test
    # We want to verify the AGENT'S DECISION to call tools.
    
    # 1. Test "Focus Mode" (Reaction to user request)
    print("\n[Scenario 1] User: 'I need to focus, don't remind me.'")
    
    # We'll mock the LLM response to simulate the agent deciding to call the tool
    # But wait, we want to test the REAL agent logic (including prompt). 
    # Since we can't easily mock the LLM's *decision* without a real LLM, 
    # we will rely on the real LLM (Gemini) but mock the *tools* to verify they were called.
    
    # Mock Tool Execution to spy on calls
    # Note: In LangGraph, tools are bound. We can't easily mock them inside the compiled graph 
    # without rebuilding it. 
    # Instead, we will run the agent and check the output messages for tool calls.
    
    inputs = {"messages": [HumanMessage(content="I need to focus, stop sending me alerts for a while.")], "user_profile": ""}
    
    # We expect the agent to call `set_preference` or `set_risk_override`
    # Since we are using the real LLM, this is an integration test.
    
    try:
        result = await liaison_agent.ainvoke(inputs)
        last_msg = result["messages"][-1]
        print(f"Agent Response: {last_msg.content}")
        
        # Check if tool was called (heuristic: look for tool output in history or specific text)
        # In our Liaison implementation, tool outputs are added to messages.
        tool_outputs = [m.content for m in result["messages"] if "Tool Output" in str(m.content)]
        print(f"Tool Outputs: {tool_outputs}")
        
        if any("Preference set" in o or "Risk Override" in o for o in tool_outputs):
            print("SUCCESS: Agent correctly suppressed alerts.")
        else:
            print("WARNING: Agent did not explicitly call suppression tool. It might have just acknowledged.")

    except Exception as e:
        print(f"FAILURE: {e}")

    # 2. Test "What did I do?" (Complex Query)
    print("\n[Scenario 2] User: 'Read your knowledge graph and memory, what have I done recently?'")
    
    # Seed a unique memory to verify retrieval
    await hippocampus.add_memory("User ate a purple banana for breakfast.")
    
    inputs = {"messages": [HumanMessage(content="Read your knowledge graph and memory, what have I done recently?")], "user_profile": ""}
    
    try:
        result = await liaison_agent.ainvoke(inputs)
        
        print("\n--- Full Message History ---")
        for m in result["messages"]:
            print(f"[{m.type}] {m.content[:100]}...")
            
        tool_outputs = [m.content for m in result["messages"] if "Tool Output" in str(m.content)]
        
        # We expect query_graph or manage_memory(search)
        if any("purple banana" in o for o in tool_outputs):
             print("SUCCESS: Agent queried graph/memory and found the purple banana.")
        elif any("Graph Analysis" in o or "Memory Search" in o for o in tool_outputs):
             print("PARTIAL SUCCESS: Agent called tool but maybe didn't find the specific memory.")
        else:
             print("FAILURE: Agent did not query graph/memory.")

    except Exception as e:
        print(f"FAILURE: {e}")

    # 3. Test "Work History" (Multilingual & Duration)
    print("\n[Scenario 3] User: '请给出我最近工作的具体内容和具体时间段' (Chinese Query)")
    
    inputs = {"messages": [HumanMessage(content="请给出我最近工作的具体内容和具体时间段比如：几点到几点进行了什么工作？")], "user_profile": ""}
    
    try:
        result = await liaison_agent.ainvoke(inputs)
        
        print("\n--- Full Message History (Scenario 3) ---")
        for m in result["messages"]:
            print(f"[{m.type}] {m.content[:100]}...")
            
        tool_outputs = [m.content for m in result["messages"] if "Tool Output" in str(m.content)]
        
        # We expect query_graph to be called and return "Recent Timeline"
        if any("Recent Timeline" in o for o in tool_outputs):
             print("SUCCESS: Agent queried graph and got timeline.")
             if "Duration:" in tool_outputs[0]:
                 print("SUCCESS: Duration info present in tool output.")
        else:
             print("FAILURE: Agent did not query graph or get timeline.")

    except Exception as e:
        print(f"FAILURE: {e}")

if __name__ == "__main__":
    asyncio.run(test_autonomy())
