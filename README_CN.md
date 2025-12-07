# VitalSense: 有感知的健康推理智能体 (The Sentient Health Inference Agent)

> **"高度自主。高度智能。高度敏锐。"**

[English](README.md) | [中文文档](README_CN.md)

**VitalSense** 是一个实验性的 **自主多智能体健康操作系统 (VitalOS)**，旨在成为您私有、有感知的数字健康孪生体。与被动的健康追踪器不同，VitalSense 主动感知您的数字环境，利用智能体议会 (Council of Agents) 推理您的健康状况，并在您精疲力竭之前主动进行干预。

---

## 🌟 核心理念

VitalSense 超越了简单的问答机器人，进化为 **有感知的私人助理**：

1.  **高度自主 (High Autonomy)**：它管理自己的记忆，决定何时说话，并尊重您的专注模式。它不会等您求助——当检测到风险时，它会主动介入。
2.  **高度智能 (High Intelligence)**：由 **GraphRAG** (图检索增强生成) 驱动，它能理解上下文，计算活动时长，并检测复杂的行为模式（例如“过度劳累”）。
3.  **高度敏锐 (High Perception)**：它能“看”到您的屏幕（注重隐私的本地分析）并“记住”您的历史，从而构建一个持久、进化的用户模型。
4.  **混合大脑 (Hybrid Brain)**：无缝切换 **Google Gemini** (云端) 和 **Local LLMs** (通过 LM Studio/Ollama 本地运行)，实现完全的隐私和控制。

---

## 🏗 系统架构

### 大脑 (Backend)
*   **智能体框架**: 基于 **LangGraph** 构建，用于复杂的多步推理。
*   **记忆系统**: **ChromaDB** (向量存储) + **NetworkX** (知识图谱) 用于深度情景和语义记忆。
*   **议会 (The Council)**: 一群专业的智能体：
    *   **Liaison (联络员)**: 您的主要接口（高度自主）。
    *   **Dr. Nexus (医生)**: 生理分析。
    *   **Guardian (守护者)**: 安全与风险评估。
    *   **Maestro (指挥家)**: 控制您的环境（例如屏幕亮度、智能灯光）。

### 面孔 (Frontend)
*   **技术栈**: Next.js, TypeScript, Tailwind CSS, Framer Motion.
*   **美学风格**: "数字粗野主义 (Digital Brutalism)" 遇上 "玻璃拟态 (Glassmorphism)"。
*   **关键特性**:
    *   **3D 记忆星系**: 可视化您的思维模式。
    *   **风险卡片 (Risk Cards)**: 交互式、非侵入性的健康干预。
    *   **实时时间轴**: 一眼掌握您的一天。

---

## 🚀 快速开始

### 前置要求
*   Python 3.10+
*   Node.js 18+
*   **Google Gemini API Key** (云端模式) 或 **LM Studio** (本地模式)

### 1. 后端设置

```bash
cd backend
pip install -r requirements.txt
```

#### 选项 A: 云端模式 (Gemini) - *推荐用于速度*
```bash
export GOOGLE_API_KEY="your_api_key_here"
export LLM_PROVIDER="gemini" # 默认
python -m backend.main
```

#### 选项 B: 本地模式 (隐私优先)
1.  启动 **LM Studio** 并加载模型 (例如 `Qwen-2.5-7b-instruct`)。
2.  启动 **Local Server** (默认端口 `1234`)。
3.  运行 VitalSense:
    ```bash
    export LLM_PROVIDER="local"
    # 可选: 如果需要自定义 URL/模型
    # export LOCAL_LLM_URL="http://localhost:1234/v1"
    python -m backend.main
    ```

### 2. 前端设置

```bash
cd frontend
npm install
npm run dev
```

访问 `http://localhost:3000` 来见见您新的感知助手吧。

---

## 🧠 关键特性

### 🔍 GraphRAG & 深度回忆
问它 *“我最近做了什么？”*，VitalSense 会遍历其知识图谱，为您提供基于时间的活动摘要，而不仅仅是关键词匹配。

### 👁️ 本地视觉 (Local Vision)
VitalSense 可以“看”您的屏幕以检测疲劳或压力诱因。在 **本地模式** 下，截图完全在您的机器上使用具备视觉能力的模型（如 Qwen-VL）进行分析，确保零数据泄露。

### 🛡️ 议会 (The Council)
您的健康数据由一组 AI 专家进行辩论。如果 **医生** 检测到眼疲劳，但 **守护者** 看到您处于“专注模式”，它们会协商出最佳的干预策略。

---

## 📜 许可证
MIT License. Created by Antigravity (Google Deepmind) & The User.
