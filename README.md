# VitalSense: The Sentient Health Inference Agent

> **"Highly Autonomous. Highly Intelligent. Highly Perceptive."**

**VitalSense** is an experimental **Autonomous Multi-Agent Health Operating System (VitalOS)** designed to be your private, sentient digital health twin. Unlike passive trackers, VitalSense actively perceives your digital environment, reasons about your well-being using a Council of Agents, and intervenes proactively to prevent burnout.

---

## 🌟 Core Philosophy

VitalSense evolves beyond simple command-response bots into a **Sentient Private Assistant**:

1.  **High Autonomy**: It manages its own memory, decides when to speak, and respects your focus. It doesn't wait for you to ask for help—it steps in when it detects risk.
2.  **High Intelligence**: Powered by **GraphRAG** (Graph Retrieval-Augmented Generation), it understands context, calculates activity durations, and detects complex behavioral patterns (e.g., "The Grind").
3.  **High Perception**: It "sees" your screen (privacy-focused local analysis) and "remembers" your history to build a persistent, evolving model of you.
4.  **Hybrid Brain**: Seamlessly switch between **Google Gemini** (Cloud) and **Local LLMs** (via LM Studio/Ollama) for complete privacy and control.

---

## 🏗 System Architecture

### The Brain (Backend)
*   **Agent Framework**: Built on **LangGraph** for complex, multi-step reasoning.
*   **Memory**: **ChromaDB** (Vector Store) + **NetworkX** (Knowledge Graph) for deep episodic and semantic memory.
*   **The Council**: A swarm of specialized agents:
    *   **Liaison**: Your primary interface (highly autonomous).
    *   **Dr. Nexus**: Physiological analysis.
    *   **Guardian**: Safety and risk assessment.
    *   **Maestro**: Controls your environment (e.g., screen brightness, smart lights).

### The Face (Frontend)
*   **Tech Stack**: Next.js, TypeScript, Tailwind CSS, Framer Motion.
*   **Aesthetic**: "Digital Brutalism" meets "Glassmorphism".
*   **Key Features**:
    *   **3D Memory Galaxy**: Visualize your own thought patterns.
    *   **Risk Cards**: Interactive, non-intrusive health interventions.
    *   **Real-time Timeline**: See your day at a glance.

---

## 🚀 Getting Started

### Prerequisites
*   Python 3.10+
*   Node.js 18+
*   **Google Gemini API Key** (for Cloud mode) OR **LM Studio** (for Local mode)

### 1. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

#### Option A: Cloud Mode (Gemini) - *Recommended for Speed*
```bash
export GOOGLE_API_KEY="your_api_key_here"
export LLM_PROVIDER="gemini" # Default
python -m backend.main
```

#### Option B: Local Mode (Privacy Focused)
1.  Launch **LM Studio** and load a model (e.g., `Qwen-2.5-7b-instruct`).
2.  Start the **Local Server** (default port `1234`).
3.  Run VitalSense:
    ```bash
    export LLM_PROVIDER="local"
    # Optional: Customize URL/Model if needed
    # export LOCAL_LLM_URL="http://localhost:1234/v1"
    python -m backend.main
    ```

### 2. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:3000` to meet your new Sentient Assistant.

---

## 🧠 Key Features

### 🔍 GraphRAG & Deep Recall
Ask *"What have I done recently?"* and VitalSense will traverse its Knowledge Graph to give you a time-aware summary of your activities, not just a keyword match.

### 👁️ Local Vision
VitalSense can "see" your screen to detect fatigue or stress triggers. In **Local Mode**, screenshots are analyzed entirely on your machine using Vision-capable models (e.g., Qwen-VL), ensuring zero data leakage.

### 🛡️ The Council
Your health data is debated by a team of AI experts. If the **Doctor** detects eye strain but the **Guardian** sees you're in "Focus Mode," they negotiate the best intervention strategy.

---

## 📜 License
MIT License. Created by Antigravity (Google Deepmind) & The User.
