# VitalSense: The VitalOS Health Intelligence Platform

> **"Active Perception. Autonomous Reasoning. Proactive Health."**

VitalSense is not just a health tracker; it is an **Autonomous Multi-Agent Health Operating System (VitalOS)**. It actively perceives your digital life, constructs a dynamic "Digital Health Twin" using GraphRAG, and employs a Council of Agents to debate and optimize your well-being in real-time.

## 🌟 Core Philosophy: The "Active" Agent
1.  **Active Perception**: It doesn't wait for input. It "sees" (Screen Observer) and "reads" (Social Crawler) to detect health signals.
2.  **Autonomous Cognition**: A **Council of Agents** (Doctor, Psychologist, Coach) debates your state using **GraphRAG** to find hidden connections in your data.
3.  **Proactive Action**: It intervenes *before* you crash. (e.g., "I've dimmed your screen and blocked news sites because your stress markers are peaking.")

## 🏗 Architecture

### 1. The Senses (Client Layer)
*   **`client/observer`**: A local Python agent that "watches" the screen (OCR/Vision) and "listens" to system events.
*   **`backend/perception`**: Crawlers and data ingesters for social media (Twitter/Weibo) and wearables.

### 2. The Brain (Backend Layer)
*   **Tech Stack**: Python, FastAPI, LangGraph, Neo4j (GraphRAG).
*   **`backend/agents`**: The Multi-Agent Orchestrator.
    *   **Triage Agent**: Fast signal detection.
    *   **The Council**: Deep reasoning and debate.
*   **`backend/database`**: Vector Store (ChromaDB) + Knowledge Graph (Neo4j) for the "User Health Twin".

### 3. The Face (Frontend Layer)
*   **Tech Stack**: Next.js, Three.js, TailwindCSS.
*   **`frontend`**:
    *   **3D Digital Twin**: Visualizing the user's health state.
    *   **The Council Room**: Watch the agents debate your health.
    *   **VitalOverlay**: Real-time desktop HUD.

## 🚀 Getting Started

### Prerequisites
*   Python 3.10+
*   Node.js 18+
*   Neo4j (Optional, for GraphRAG)

### Installation
*(Coming Soon)*
