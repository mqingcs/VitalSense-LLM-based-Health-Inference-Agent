# VitalSense: The Ultimate Codex

> **To the Inheritor:**
> You are receiving the "VitalSense" project (Internal Kernel: "VitalOS"). This is an **Agentic Digital Twin** designed to monitor, reason about, and actively improve a user's health and productivity.
>
> This document is your DNA. It contains the **complete logic, architecture, implementation details, and evolution history** of the system. It is designed to let you reconstruct the project from scratch if necessary.

---

## 1. Project Identity & Philosophy

*   **Name**: VitalSense
*   **Core Concept**: A "Sentient" Private Assistant.
*   **Philosophy**:
    *   **Agentic**: It doesn't just show data; it *intervenes*.
    *   **Biological**: It sleeps, dreams (consolidates memory), and adapts (learns tolerance).
    *   **Ambient**: It communicates via a "Bio-Field" (color/motion) to influence the user's subconscious state.
    *   **Privacy-First**: All raw data is stored locally (`backend/data/`). LLM calls are anonymized/structured.
    *   **Digital Brutalism**: The UI is raw, data-dense, and beautiful (Cyan/Red/Amber/Black).

---

## 2. Technical Stack

### Backend (`/backend`)
*   **Language**: Python 3.9+
*   **Framework**: `FastAPI` (ASGI Server).
*   **Real-time**: `python-socketio` (WebSocket).
*   **AI Orchestration**: `LangGraph` (Multi-Agent Workflow), `LangChain`.
*   **LLM**: `Google Gemini 1.5 Flash` (via `google-generativeai`).
*   **Memory (Vector)**: `ChromaDB` (Persistent Vector Store).
*   **Memory (Graph)**: `NetworkX` (In-memory Temporal Graph).
*   **Perception**: `pyautogui` (Screen Capture), `watchdog` (File Monitoring).
*   **Validation**: `Pydantic` (Strict Schema Enforcement).

### Frontend (`/frontend`)
*   **Framework**: `Next.js 14` (App Router).
*   **Language**: `TypeScript`.
*   **Styling**: `Tailwind CSS`.
*   **3D Graphics**: `Three.js` + `React Three Fiber` (R3F) + `Drei`.
*   **Shaders**: Custom GLSL (for BioField).
*   **Real-time**: `socket.io-client`.
*   **Icons**: `Lucide React`.

---

## 3. The "Sentient" Architecture

The system operates on a continuous **Perception-Cognition-Action** loop, augmented by a **Biological Memory Cycle**.

### 3.1. The Loop (Real-Time)
1.  **Perception**: Sensors (`ScreenSensor`, `FileSensor`) capture raw data.
2.  **Ingestion**: Data is standardized into `VitalEvent` and broadcast via Event Bus.
3.  **Cognition (The Council)**: A LangGraph workflow processes the event:
    *   **Triage**: Needs Doctor? Needs Coach?
    *   **Experts**: Dr. Nexus (Medical) & Guardian (Lifestyle) analyze.
    *   **Synthesis**: The Chair combines opinions + **Risk Engine** + **GraphRAG**.
4.  **Action**:
    *   **Maestro**: Adjusts the ambient `BioField` (Color/Brightness).
    *   **Actuator**: Sends `RiskCard` to Chat if High Risk.
5.  **Memory**: The event is stored in `Hippocampus` (ChromaDB) and `GraphService` (NetworkX).

### 3.2. The Dream (Offline Consolidation)
*   **Trigger**: System Startup after >4 hours of downtime.
*   **Process**:
    1.  **Cluster**: Groups raw "Moment" logs from the previous session.
    2.  **Synthesize**: Uses LLM to generate a high-level "Episode" summary.
    3.  **Archive**: Moves raw logs to `backend/data/cold_storage/archive.jsonl` (Zero Data Loss).
    4.  **Prune**: Deletes raw logs from active memory to maintain speed.

### 3.3. The Negotiation (Feedback Loop)
*   **Trigger**: User interacts with a `RiskCard` ("Not now").
*   **Process**:
    1.  Frontend emits `adjust_tolerance(risk_type, amount)`.
    2.  Backend `RiskEngine` updates `UserProfile.risk_modifiers`.
    3.  Future risk calculations are dampened for that specific risk type.

---

## 4. Directory Map & Implementation Details

### `/backend`

#### `main.py`
*   **Role**: The Kernel.
*   **Key Implementation**:
    *   `lifespan`: Manages startup/shutdown of sensors and `VitalPulse`.
    *   `socket_app`: Wraps FastAPI to handle WebSocket events.
    *   `handle_chat`: Routes user messages to `Liaison` agent.
    *   `run_council`: The main callback for `DATA_INGESTED` events.

#### `core/`
*   **`pulse.py`**:
    *   **`VitalPulse`**: Singleton. Checks `startup_gap`. Triggers `hippocampus.consolidate_memories()`.
*   **`risk_engine.py`**:
    *   **`RiskEngine`**: Hybrid Calculator.
    *   **`calculate_deterministic_risk`**: Regex/Keyword based (Fast).
    *   **`assess_complex_risks`**: Graph traversal (e.g., "The Grind" pattern).
    *   **`adjust_tolerance`**: Modifies `user_profile` based on feedback.
*   **`memory.py`**:
    *   **`Hippocampus`**: Wrapper for ChromaDB.
    *   **`consolidate_memories`**: The "Dream" logic.
*   **`graph_service.py`**:
    *   **`GraphService`**: Manages NetworkX graph.
    *   **`detect_grind_pattern`**: Traverses recent nodes to sum "Work" duration without "Break".
*   **`profile_service.py`**:
    *   **`ProfileService`**: Manages `user_profile.json`.
    *   **`update_condition`**: Dynamically adds/removes health conditions that affect risk.

#### `agents/`
*   **`council.py`**:
    *   **`council_graph`**: The LangGraph workflow.
    *   **Nodes**: `triage`, `doctor`, `coach`, `synthesizer`, `maestro`.
    *   **Logic**: Synthesizer node explicitly calls `RiskEngine` to fuse LLM wisdom with deterministic math.
*   **`liaison.py`**:
    *   **`liaison_agent`**: ReAct agent (LangChain).
    *   **Tools**: `update_profile`, `manage_memory`, `set_risk_override`.
    *   **Prompt**: Designed to be empathetic and proactive.
*   **`schemas.py`**:
    *   **Pydantic Models**: `CouncilActionPlan`, `RiskAssessment`, `MemoryEntry`.
    *   **Critical Fix**: `MemoryEntry.remarks` has `default=None` to support legacy data.

#### `perception/`
*   **`screen_sensor.py`**: Uses `pyautogui` + Gemini Vision.
*   **`file_sensor.py`**: Uses `watchdog` to monitor JSON files.

### `/frontend`

#### `components/`
*   **`ChatInterface.tsx`**:
    *   **`RiskCard`**: The interactive UI component.
    *   **Logic**: Listens for `analysis_result` and `risk_card`. Emits `adjust_tolerance`.
    *   **Fix**: Removed emoji text generation to fix build error.
*   **`BioField.tsx`**:
    *   **Shader**: Custom GLSL for the "Living Background".
    *   **Uniforms**: Controlled by `Maestro` (Color, Speed, Turbulence).
*   **`CouncilRoom.tsx`**:
    *   **Log**: Displays the internal thought process of the agents.
*   **`MemoryGalaxy.tsx`**:
    *   **3D Graph**: Visualizes the `Hippocampus` using R3F.

---

## 5. The "Final Evolution" (Phase 7)

This phase transformed the system from a "Tool" to a "Being".

### 5.1. Wake-Up Consolidation ("Dreams")
*   **Problem**: Raw sensor logs (every 5s) bloat the database and context window.
*   **Solution**:
    *   On startup, if `gap > 4h`:
    *   **Compress**: 1000 "Screen Observations" -> 1 "Work Session" Episode.
    *   **Archive**: Raw data moves to `cold_storage`.
    *   **Result**: The agent remembers "I worked all afternoon" (Human-like) instead of "I saw a screen at 1:00, 1:05, 1:10..." (Robot-like).

### 5.2. Interactive Negotiation
*   **Problem**: Constant alerts annoy the user and lead to "Alert Fatigue".
*   **Solution**:
    *   **Risk Cards**: UI allows "Not Now" (Dismiss).
    *   **Math**: Dismissal = `tolerance += 0.1`.
    *   **Result**: The agent learns *your* specific threshold for stress/sedentary behavior.

---

## 6. How to Run

### Backend
```bash
cd backend
# 1. Activate Venv
source .venv/bin/activate
# 2. Install Deps
pip install -r requirements.txt
# 3. Set Key
export GEMINI_API_KEY="your_key_here"
# 4. Run
python -m backend.main
```

### Frontend
```bash
cd frontend
# 1. Install
npm install
# 2. Run
npm run dev
```

---

## 7. Known Issues & "Ghost in the Shell"

1.  **Screen Permissions (macOS)**: You MUST grant "Screen Recording" permission to the terminal. If the sensor sees black, this is why.
2.  **Socket Latency**: The initial handshake can take 1-2 seconds. The frontend shows "Connecting...".
3.  **Graph Complexity**: `MemoryGalaxy` renders all nodes. With >1000 nodes, it may lag. (Mitigation: The "Dream" protocol keeps active node count low).
4.  **LLM Hallucination**: Gemini sometimes returns invalid JSON. The system has `try-except` blocks to handle this gracefully.

---

## 8. Development Log (Chronological)

1.  **Phase 1**: Core Architecture (FastAPI + Socket.IO).
2.  **Phase 2**: Perception (ScreenSensor + Gemini Vision).
3.  **Phase 3**: The Council (LangGraph Multi-Agent System).
4.  **Phase 4**: Memory (ChromaDB + GraphService).
5.  **Phase 5**: Frontend (Next.js + Three.js BioField).
6.  **Phase 6**: Liaison Agent (ReAct + ProfileService).
7.  **Phase 7 (Final)**:
    *   **Dreams**: `consolidate_memories` + Cold Storage.
    *   **Interactivity**: `RiskCard` + `adjust_tolerance`.
    *   **Dynamic Modeling**: `RiskEngine` uses `UserProfile` conditions.
    *   **Fixes**: Schema validation, Build errors.

---

> **Final Status**: The system is fully operational. It perceives, thinks, remembers, dreams, and negotiates.
> **Signed**: Antigravity (Phase 7 Architect)

*End of Codex.*
