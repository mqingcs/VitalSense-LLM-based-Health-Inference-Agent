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

from backend.core.actuators import NotificationActuator
from backend.core.memory import hippocampus

# --- Socket.IO Setup ---
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

# --- Lifecycle Manager ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("--- [VitalOS] System Boot Sequence Initiated ---")
    
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
            
        # 4. Long-term Memory Storage
        # Construct a full log for the Hippocampus to analyze
        full_log = f"""
        Timestamp: {datetime.now().isoformat()}
        Input Source: {event.payload['type']}
        Input Text: {event.payload['text']}
        Risk Level: {final_plan.risk_level}
        Summary: {final_plan.summary}
        Actions: {final_plan.actions}
        """
        await hippocampus.add_memory(full_log)
        
    event_bus.subscribe(EventType.DATA_INGESTED, run_council)
    
    yield
    
    # Shutdown
    print("--- [VitalOS] System Shutdown ---")
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
    Returns the full Memory Graph for visualization.
    """
    memories = await hippocampus.get_all_memories()
    
    # Transform into Graph format (Nodes + Links)
    nodes = []
    links = []
    
    for m in memories:
        # Node
        nodes.append({
            "id": m.timestamp,
            "group": 1 if "High" in m.outcome else (2 if "Medium" in m.outcome else 3), # Color by risk (heuristic)
            "label": m.statement,
            "details": m.model_dump()
        })
    
    # Generate Links based on shared entities
    for i in range(len(memories)):
        for j in range(i + 1, len(memories)):
            m1 = memories[i]
            m2 = memories[j]
            
            # Find intersection of entities
            shared = set(m1.entities).intersection(set(m2.entities))
            if shared:
                links.append({
                    "source": m1.timestamp,
                    "target": m2.timestamp,
                    "value": len(shared)
                })

    return {"nodes": nodes, "links": links}

if __name__ == "__main__":
    # Run socket_app instead of app
    uvicorn.run("backend.main:socket_app", host="0.0.0.0", port=8000, reload=True)
