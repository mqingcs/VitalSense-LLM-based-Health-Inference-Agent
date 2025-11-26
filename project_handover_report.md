# VitalSense: The Complete Project Codex

> **To the Inheritor:**
> This is not just a report; it is the DNA of VitalSense. It contains the complete logic, architecture, and implementation details of every single component in the system. Use this to reconstruct, debug, or evolve the system without ambiguity.

---

## 1. Project Identity & Philosophy

*   **Name**: VitalSense (Internal Kernel: "VitalOS")
*   **Mission**: To create an **Agentic Digital Twin** that monitors, reasons about, and actively improves the user's health and productivity.
*   **Core Philosophy**:
    *   **Agentic**: Proactive intervention over passive display.
    *   **Ambient**: Information is conveyed through "Bio-Field" (color/motion) rather than just numbers.
    *   **Privacy-First**: Local-first processing; secure LLM calls.
    *   **Digital Brutalism**: High-contrast, raw, data-dense aesthetic (Cyan/Red/Black).

---

## 2. System Architecture: The Loop

The system operates on a continuous **Perception-Cognition-Action** loop:

1.  **Perception (Sensors)**:
    *   **ScreenSensor**: Captures visual context (what is the user doing?).
    *   **FileSensor**: Ingests external health data (JSON).
2.  **Ingestion (Event Bus)**:
    *   Standardizes data into `VitalEvent` objects.
    *   Broadcasts via `socket.io` to Frontend and Agents.
3.  **Cognition (The Brain)**:
    *   **The Council**: A LangGraph multi-agent system for immediate risk assessment.
    *   **The Liaison**: A ReAct agent for user interaction and long-term profile management.
4.  **Memory (The Soul)**:
    *   **Hippocampus**: Episodic memory (Vector Store).
    *   **GraphService**: Temporal Knowledge Graph (Pattern Detection).
    *   **ProfileService**: User Traits & Preferences (JSON).
5.  **Action (Effectors)**:
    *   **Maestro**: Controls the ambient environment (Bio-Field).
    *   **Actuators**: Physical system changes (Notifications, Brightness).
    *   **Chat**: Direct communication with the user.

---

## 3. Backend Implementation Details (`backend/`)

### 3.1. Core Infrastructure
*   **`main.py`**: The central nervous system.
    *   **FastAPI App**: Serves API endpoints (`/memories`, `/delete_memory`).
    *   **Socket.IO Server**: Handles real-time events (`connect`, `sensor_data`, `chat_message`).
    *   **Event Loop**: Orchestrates `screen_sensor` and `file_sensor` background tasks.
    *   **Integration**: Connects `Council` and `Liaison` to the data stream.
*   **`core/event_bus.py`**:
    *   **`VitalEventBus`**: Singleton publisher/subscriber for internal events. Decouples sensors from agents.

### 3.2. Perception Layer (`perception/`)
*   **`screen_sensor.py`**:
    *   **Logic**: Captures screen every 5 seconds using `pyautogui`.
    *   **Processing**: Resizes to thumbnail -> Base64.
    *   **Analysis**: Sends image to **Gemini 1.5 Flash** for "Activity Analysis" (Risk, Category, Description).
    *   **Output**: Emits `sensor_data` event with `type: screen_observer`.
*   **`file_sensor.py`**:
    *   **Logic**: Watches `backend/data/input.json` for changes using `watchdog`.
    *   **Output**: Emits `sensor_data` event with `type: health_monitor`.

### 3.3. Cognitive Layer (`agents/`)
#### **The Council (`council.py`)**
A **LangGraph** workflow that processes every sensor input.
*   **State**: `CouncilState` (Input, Source, Memories, Triage, Doctor, Coach, Final Output, Environment).
*   **Nodes**:
    1.  **`triage_node`**: Uses `TRIAGE_PROMPT` to route to Doctor/Coach. Recalls relevant memories.
    2.  **`doctor_node` (Dr. Nexus)**: `DOCTOR_PROMPT`. Medical analysis (Symptoms, Vitals).
    3.  **`coach_node` (Guardian)**: `COACH_PROMPT`. Lifestyle analysis (Habits, Ergonomics).
    4.  **`synthesizer_node` (Chair)**: `SYNTHESIZER_PROMPT`.
        *   Aggregates expert opinions.
        *   **Risk Engine Integration**: Calls `risk_engine.calculate_deterministic_risk` AND `assess_complex_risks` (GraphRAG).
        *   **Decision**: Produces `CouncilActionPlan` (Risk Level, Summary, Actions).
    5.  **`maestro_node`**: Maps risk/emotion to `BioField` parameters (Color, Turbulence, Brightness).
*   **Edges**: Conditional routing based on Triage -> Synthesizer -> Maestro -> End.

#### **The Liaison (`liaison.py`)**
A **ReAct** agent for user interaction.
*   **State**: `LiaisonState` (Messages, User Profile Context).
*   **Logic**:
    1.  **Context Loading**: Fetches `ProfileService.get_context_str()`.
    2.  **LLM Call**: Uses `LIAISON_PROMPT` (Persona: Empathetic, Proactive).
    3.  **ReAct Loop**:
        *   Parses JSON tool calls (e.g., `{"tool": "update_profile", ...}`).
        *   Executes tool function.
        *   Feeds result back to LLM as `HumanMessage` (Observation).
        *   Repeats until final response.
*   **Tools**: `update_profile`, `manage_memory`, `set_preference`, `query_graph`.

### 3.4. Memory Systems (`core/`)
*   **`memory.py` (Hippocampus)**:
    *   **Store**: **ChromaDB** (`vitalsense_db`).
    *   **Schema**: `MemoryEntry` (Timestamp, Statement, Entities, etc.).
    *   **Functions**: `add_memory` (Embed + Store), `recall` (Vector Search), `delete_memory` (ID/Range).
*   **`graph_service.py`**:
    *   **Store**: **NetworkX** (In-memory, rebuilt from ChromaDB).
    *   **Logic**: Nodes = Memories/Entities. Edges = Temporal/Semantic links.
    *   **Pattern Detection**:
        *   **"The Grind"**: >60m of "Work" nodes connected temporally without "Break" nodes.
        *   **"Mixed Media"**: Rapid switching between "Work" and "Entertainment" nodes.
*   **`profile_service.py`**:
    *   **Store**: `backend/data/user_profile.json`.
    *   **Schema**: `UserProfile` (Traits, Conditions, Habits, Preferences).
    *   **Logic**: CRUD operations for long-term user context.

### 3.5. Risk Engine (`core/risk_engine.py`)
*   **Hybrid Approach**:
    1.  **Deterministic**: Keyword matching (e.g., "chest pain" = +0.5, "no water" = +0.2) + Duration multipliers.
    2.  **Graph-Based**: Calls `GraphService` to detect temporal patterns ("The Grind").
*   **Output**: Combined Risk Score (0.0-1.0) and Reasoning.

### 3.6. LLM Provider (`core/llm.py`)
*   **Model**: **Google Gemini 1.5 Flash**.
*   **Wrapper**: `GeminiProvider`.
*   **Features**:
    *   `generate_chat`: Handles conversation history. **Safety**: Returns empty string on `None`.
    *   `generate_structured`: Enforces Pydantic schemas via `response_json_schema`.
    *   `analyze_image`: Multimodal input.
    *   `get_embedding`: `text-embedding-004`.

---

## 4. Frontend Implementation Details (`frontend/`)

### 4.1. Core UI Components
*   **`app/page.tsx`**: The Layout.
    *   **Structure**: `BioField` (Background) -> `DigitalTwin` + `MemoryGalaxy` (Left) -> `CouncilRoom` (Right) -> `SessionTimeline` (Bottom).
    *   **Logic**: Manages global layout and z-indexing.
*   **`ui/GlassPanel.tsx`**:
    *   **Style**: Glassmorphism (Backdrop blur, border, noise texture).
    *   **Crucial Fix**: Inner `div` has `h-full w-full` to ensure children flex layouts work.

### 4.2. Visualization Components
*   **`BioField.tsx`**:
    *   **Tech**: **Three.js (R3F)** + Custom GLSL Shader.
    *   **Uniforms**: `uColor`, `uTurbulence`, `uSpeed`.
    *   **Logic**: Listens to `environment_update` socket event from Maestro to morph the background.
*   **`MemoryGalaxy.tsx`**:
    *   **Tech**: **Three.js** + `react-three-fiber`.
    *   **Logic**: 3D Force-Directed Graph of memories.
    *   **Interaction**: Click node -> Open `MemoryManager` modal.
    *   **Updates**: Real-time addition of nodes via `memory_added` socket event.
*   **`SessionTimeline.tsx`**:
    *   **UI**: Horizontal scrollable list of "Snapshots".
    *   **Data**: Listens to `sensor_data` (Screen/File).
    *   **Logic**: Auto-scrolls to newest. Highlights risks in Red.
*   **`DigitalTwin.tsx`**:
    *   **Tech**: Three.js Sphere with pulse animation.
    *   **Logic**: Visual metaphor for core stability.

### 4.3. Interaction Components
*   **`CouncilRoom.tsx`**:
    *   **UI**: Scrolling log of agent thoughts.
    *   **Logic**: Listens to `sensor_data` (System), `analysis_result` (Chair), and agent activation events.
*   **`ChatInterface.tsx`**:
    *   **UI**: Draggable, floating chat window.
    *   **Logic**:
        *   **Drag**: Custom mouse event handlers on Header.
        *   **Chat**: Emits `chat_message`, listens for `chat_reply`.
        *   **Alerts**: Injects System Alerts (High Risk) into chat stream.
        *   **Layout**: Flex column with fixed bottom input (resolved layout bug).

---

## 5. How to Run & Develop

### Prerequisites
*   **Python 3.9+** (Backend)
*   **Node.js 18+** (Frontend)
*   **Google Gemini API Key** (`GEMINI_API_KEY` env var).

### Backend Setup
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# Ensure backend/data/ exists
python -m backend.main
```
*   **Port**: 8000
*   **Endpoints**: `ws://localhost:8000`, `http://localhost:8000/docs`

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
*   **Port**: 3000
*   **URL**: `http://localhost:3000`

---

## 6. Known Issues & "Ghost in the Shell"
1.  **Screen Permissions**: On macOS, you MUST grant Screen Recording permission to the terminal running the backend. If denied, `screen_sensor` sees black.
2.  **Socket Latency**: Initial connection might take a second. Frontend handles this with "Waiting for signal..." states.
3.  **Graph Complexity**: As memories grow, `MemoryGalaxy` performance may degrade. Needs LOD (Level of Detail) optimization in future.
4.  **LLM Hallucination**: Rarely, Gemini might output malformed JSON. The `try-except` blocks in `council.py` and `liaison.py` handle this by falling back to safe defaults.

---

## 7. Change Log (Phase 6 Final)
*   **[FEATURE] GraphRAG**: Added `GraphService` for temporal pattern detection ("The Grind").
*   **[FEATURE] Liaison Agent**: Added ReAct-based chat agent with `ProfileService` integration.
*   **[FIX] Chat Layout**: Fixed `ChatInterface` scrolling and input positioning via `GlassPanel` CSS update.
*   **[FIX] Timeline Layout**: Integrated `SessionTimeline` into page flow, removed fixed positioning.
*   **[FIX] Stability**: Resolved `NameError` in `main.py`/`profile_service.py` and `TypeError` in `liaison.py` (NoneType response).

---

> **Final Status**: The system is fully operational. It perceives, thinks, remembers, and speaks.
> **Signed**: Antigravity (Phase 6 Architect)

*End of Codex.*
