# VitalSense: The Sentient Health Inference Agent
## Comprehensive Project Guide & Developer Handbook

> **"Highly Autonomous. Highly Intelligent. Highly Perceptive."**

This document serves as the ultimate source of truth for the **VitalSense** project. It details the architectural vision, core components, implementation specifics, and the evolutionary path of the agent. It is designed to allow any developer (or AI agent) to instantly grasp the system's complexity and continue its development.

---

## 1. Project Vision & Core Philosophy

The goal of VitalSense is not just to be a "chatbot" or a "health tracker," but to be a **Sentient Private Assistant**.

### The "Sentient" Trinity
1.  **High Autonomy**: The agent acts without constant prompting. It manages its own memory (consolidation), suppresses its own alerts when asked ("Focus Mode"), and decides which tools to use to solve complex problems.
2.  **High Intelligence**: It doesn't just match keywords. It performs **GraphRAG** (Graph Retrieval-Augmented Generation) to understand context, calculates time durations, detects complex patterns (e.g., "The Grind"), and synthesizes multi-modal data.
3.  **High Perception**: It "sees" everything—user messages, screen activity (simulated), physiological states (inferred)—and builds a persistent, evolving model of the user (`UserProfile`).

---

## 2. System Architecture

The project follows a modern **Client-Server** architecture with a heavy emphasis on **Agentic AI** in the backend.

### Frontend (The "Face")
*   **Tech Stack**: Next.js (React), TypeScript, Tailwind CSS, Framer Motion.
*   **Design Language**: "Digital Brutalism" meets "Glassmorphism". Dark mode, neon accents, blur effects, and smooth animations.
*   **Key Components**:
    *   `ChatInterface.tsx`: The main communication hub. Renders rich UI elements like `RiskCard`.
    *   `RiskCard.tsx`: An interactive, glass-morphic card for health interventions. Supports "Dismiss" (adjusts tolerance) and "Acknowledge" actions.
    *   `SessionTimeline.tsx`: Visualizes the user's activity history.
    *   `MemoryGalaxy.tsx`: A 3D/2D visualization of the Knowledge Graph.

### Backend (The "Brain")
*   **Tech Stack**: Python (FastAPI), LangGraph, LangChain, ChromaDB, NetworkX.
*   **Communication**: Socket.IO for real-time, bi-directional events (`analysis_result`, `risk_card`).
*   **Agent Framework**: **LangGraph** is used to orchestrate the multi-agent workflow.

---

## 3. Core Modules (The "Organs")

### A. Hippocampus (Memory System)
*   **File**: `backend/core/memory.py`
*   **Role**: Manages Episodic Memory.
*   **Tech**: ChromaDB (Vector Store).
*   **Features**:
    *   **`add_memory()`**: Embeds and stores user events.
    *   **`recall()`**: Semantic search for relevant past events.
    *   **`consolidate_memories()`**: The "Sleep" function. Runs on startup if a >4h gap is detected. Clusters recent memories, synthesizes them into high-level insights, and archives raw data to `cold_storage/`.

### B. GraphService (Knowledge Graph)
*   **File**: `backend/core/graph_service.py`
*   **Role**: Manages the Semantic Knowledge Graph.
*   **Tech**: NetworkX.
*   **Features**:
    *   **`add_memory_node()`**: Converts linear memories into a graph structure (Nodes: Memory, Entity, Activity; Edges: MENTIONS, HAS_ATTRIBUTE).
    *   **`detect_grind_pattern()`**: Traverses the graph to find continuous blocks of "sedentary" or "work" nodes.
    *   **`get_recent_activity()`**: **[NEW]** Calculates the duration of recent events and returns a timeline. Used for answering "What did I do recently?".

### C. RiskEngine (The "Amygdala")
*   **File**: `backend/core/risk_engine.py`
*   **Role**: Assesses health risks in real-time.
*   **Features**:
    *   **`assess_risk()`**: Calculates risk scores based on user activity and `UserProfile` modifiers.
    *   **`adjust_tolerance()`**: **[NEW]** The feedback loop. If a user dismisses a card, the engine *lowers* the sensitivity for that risk type (e.g., "sedentary" modifier 1.0 -> 0.9).
    *   **`set_override()`**: Allows the Liaison agent to suppress specific risks for a set duration (Focus Mode).

### D. ProfileService (The "Ego")
*   **File**: `backend/core/profile_service.py`
*   **Role**: Manages the persistent `UserProfile`.
*   **Schema**:
    *   `name`, `role` (e.g., "Software Engineer").
    *   `traits`, `conditions` (e.g., "Back Pain"), `habits`.
    *   `preferences` (e.g., `mute_alerts`).
    *   `risk_modifiers` (Dynamic multipliers).

---

## 4. The Agent Swarm

### 1. Liaison Agent (The "Frontman")
*   **File**: `backend/agents/liaison.py`
*   **Role**: The primary interface with the user. It is **highly autonomous**.
*   **Tools**:
    *   `query_graph`: **[Smart Tool]** Combines timeline analysis (structure) and semantic search (content) to answer complex queries.
    *   `set_preference`: Mutes alerts/changes settings.
    *   `manage_memory`: Searches/Deletes memories.
    *   `update_profile`: Learns new user traits/conditions.
*   **Behavior**: It uses a ReAct loop to "think" before answering. It can chain tools (e.g., check profile -> query graph -> answer).

### 2. Council Agent (The "Subconscious")
*   **File**: `backend/agents/council.py`
*   **Role**: Runs in the background to analyze deeper patterns.
*   **Personas**:
    *   **Dr. Nexus**: Medical/Physiological analysis.
    *   **Guardian**: Safety/Risk analysis.
    *   **Chair**: Synthesizes inputs into a `CouncilActionPlan`.

---

## 5. Key Workflows & Features

### 1. The "Wake-Up" Consolidation Protocol
*   **Trigger**: System startup.
*   **Logic**: Checks time since last shutdown. If > 4 hours, triggers `hippocampus.consolidate_memories()`.
*   **Outcome**: Raw memories are summarized into "Daily Insights" and moved to cold storage, keeping the active context window clean and efficient.

### 2. Interactive Feedback Loop
*   **Trigger**: User clicks "Dismiss" on a `RiskCard` in the frontend.
*   **Flow**: Frontend emits `risk_response` -> Backend calls `risk_engine.adjust_tolerance()` -> Risk modifier for that category is reduced.
*   **Result**: The system "learns" not to annoy the user about that specific issue.

### 3. Autonomy: Focus Mode
*   **Trigger**: User says "I need to focus, don't remind me."
*   **Flow**: Liaison Agent recognizes intent -> Calls `set_preference('mute_alerts', 'true')` -> `ProfileService` updates preference -> `NotificationActuator` suppresses future alerts.

### 4. Intelligence: Deep Recall
*   **Trigger**: User says "What have I done recently?" (in any language).
*   **Flow**: Liaison Agent calls `query_graph` -> `GraphService` retrieves recent nodes AND calculates durations -> Agent synthesizes a detailed, time-aware response.

---

## 6. Project File Structure

```text
VitalSense/
├── backend/
│   ├── agents/
│   │   ├── council.py       # The background reasoning council
│   │   ├── liaison.py       # The main user-facing agent
│   │   ├── personas.py      # Prompts and persona definitions
│   │   └── schemas.py       # Pydantic models (MemoryEntry, UserProfile)
│   ├── core/
│   │   ├── memory.py        # Hippocampus (ChromaDB)
│   │   ├── graph_service.py # Knowledge Graph (NetworkX)
│   │   ├── risk_engine.py   # Risk assessment logic
│   │   ├── profile_service.py # User profile management
│   │   ├── enricher.py      # LLM-based entity extraction
│   │   └── llm.py           # LLM provider (Gemini)
│   ├── data/                # Persistent storage (JSON, ChromaDB)
│   └── main.py              # FastAPI app & Socket.IO server
├── frontend/
│   ├── components/
│   │   ├── ChatInterface.tsx # Main chat UI
│   │   ├── RiskCard.tsx      # Interactive intervention card
│   │   └── ...
│   └── ...
├── tests/
│   ├── test_autonomy.py      # Verification for agent autonomy
│   ├── test_final_evolution.py # Verification for consolidation & feedback
│   └── ...
└── guide.md                  # THIS FILE
```

---

## 7. Setup & Run

### Prerequisites
*   Python 3.10+
*   Node.js 18+
*   Gemini API Key

### Backend
```bash
cd backend
pip install -r requirements.txt
export GOOGLE_API_KEY="your_key"
python main.py
```

### Local LLM Support (LM Studio / Qwen)
To use a local model (e.g., Qwen via LM Studio) instead of Gemini:
1.  **LM Studio**: Load your model and start the Local Server (default port 1234).
2.  **Environment**: Set the following variables:
    ```bash
    export LLM_PROVIDER="local"
    export LOCAL_LLM_URL="http://localhost:1234/v1"
    export LOCAL_LLM_MODEL="qwen-2.5-7b-instruct" # Optional, matches your loaded model
    ```
3.  **Run**: Start the backend as usual. The system will auto-detect the provider.

### Frontend
```bash
cd frontend
npm install
npm run dev
```

---

## 8. Future Roadmap

1.  **Wearable Integration**: Connect `RiskEngine` to real-time heart rate/HRV data.
2.  **Voice Interface**: Add STT/TTS to the Liaison Agent.
3.  **Visual Perception**: Allow the agent to "see" the user via webcam for posture correction.

---
*Created by Antigravity (Google Deepmind) & The User.*
