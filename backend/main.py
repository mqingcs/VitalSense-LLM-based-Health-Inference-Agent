from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import asyncio
import socketio
from datetime import datetime
from contextlib import asynccontextmanager

from backend.core.events import event_bus, Event, EventType
from backend.perception.mock_sensor import MockSensor
from backend.perception.screen_sensor import ScreenSensorComplete as ScreenSensor
from backend.perception.file_sensor import FileSensor
from backend.agents.council import council_graph
from backend.agents.liaison import liaison_agent, LiaisonState
from langchain_core.messages import HumanMessage

from backend.core.actuators import NotificationActuator
from backend.core.memory import hippocampus

# --- Socket.IO Setup ---
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

# --- Lifecycle Manager ---
from backend.core.pulse import vital_pulse

# --- Lifecycle Manager ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("--- [VitalOS] System Boot Sequence Initiated ---")
    
    # 0. Initialize Pulse (Heartbeat)
    vital_pulse.socket_manager = sio
    pulse_task = asyncio.create_task(vital_pulse.start())
    
    # 1. Initialize Sensors & Actuators
    # mock_sensor = MockSensor(event_bus)
    # await mock_sensor.start()
    
    screen_sensor = ScreenSensor(event_bus, interval=30) 
    await screen_sensor.start()
    
    file_sensor = FileSensor(event_bus)
    await file_sensor.start()
    
    notifier = NotificationActuator()
    
    # 2. Subscribe The Council
    async def run_council(event: Event):
        print(f"--- [VitalOS] Dispatching to Council: {event.payload['text'][:30]}... ---")
        
        # Emit to Frontend
        await sio.emit('sensor_data', event.payload)
        
        inputs = {"input_data": event.payload["text"], "source": event.payload["type"]}
        
        # Run LangGraph
        result = await council_graph.ainvoke(inputs)
        
        # Parse result
        final_data = result.get("final_output")
        from backend.agents.schemas import CouncilActionPlan
        final_plan = CouncilActionPlan(**final_data)
        
        print(f"--- [VitalOS] Council Decision: {final_plan.risk_level} Risk. Actions: {final_plan.actions} ---")
        
        # Emit to Frontend
        await sio.emit('analysis_result', final_data)
        
        # 3. Active Intervention
        if final_plan.risk_level == "HIGH":
            print("!!! HIGH RISK DETECTED - INTERVENING !!!")
            await notifier.execute(final_plan)
            await sio.emit('intervention', final_data)
            
    # 5. Chat Handler
    @sio.on('chat_message')
    async def handle_chat(sid, data):
        print(f"--- [Liaison] User Message: {data['message']} ---")
        
        # Run Liaison Agent
        inputs = {"messages": [HumanMessage(content=data['message'])], "user_profile": ""}
        result = await liaison_agent.ainvoke(inputs)
        
        response = result["messages"][-1].content
        print(f"--- [Liaison] Reply: {response} ---")
        
        await sio.emit('chat_reply', {"message": response}, to=sid)
            
        # 4. Long-term Memory Storage
        # Construct a full log for the Hippocampus to analyze
        full_log = f"""
        Timestamp: {datetime.now().isoformat()}
        Input Source: chat
        Input Text: {data['message']}
        Agent Reply: {response}
        """
        await hippocampus.add_memory(full_log)
        
    event_bus.subscribe(EventType.DATA_INGESTED, run_council)
    
    yield
    
    # Shutdown
    print("--- [VitalOS] System Shutdown ---")
    vital_pulse.stop()
    pulse_task.cancel()
    # await mock_sensor.stop()
    await screen_sensor.stop()
    await file_sensor.stop()

app = FastAPI(
    title="VitalOS Kernel",
    description="The Cognitive Core of the VitalSense Health Intelligence Platform.",
    version="0.1.0",
    lifespan=lifespan
)

# CORS - Allow Frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Wrap with Socket.IO
socket_app = socketio.ASGIApp(sio, app)

@app.get("/")
async def root():
    return {
        "system": "VitalOS",
        "status": "ONLINE",
        "message": "Active Perception Systems Initialized."
    }

@app.get("/health-check")
async def health_check():
    """
    Simple heartbeat for the overlay/frontend.
    """
    return {"status": "healthy", "agents_active": True}

@app.get("/memories")
async def get_memories():
    """
    Returns all memories.
    """
    return await hippocampus.get_all_memories()

@app.delete("/memories/all")
async def clear_all_memories():
    success = await hippocampus.clear_all()
    return {"success": success}

@app.delete("/memories/range")
async def delete_memories_range(start: str, end: str):
    success = await hippocampus.delete_range(start, end)
    return {"success": success}

@app.delete("/memories/{memory_id}")
async def delete_memory(memory_id: str):
    success = await hippocampus.delete_memory(memory_id)
    return {"success": success}

@app.get("/memories/debug")
async def debug_memories():
    """
    Returns raw stats from ChromaDB to verify persistence.
    """
    return await hippocampus.get_debug_stats()

if __name__ == "__main__":
    # Run socket_app instead of app
    uvicorn.run("backend.main:socket_app", host="0.0.0.0", port=8000, reload=True)
