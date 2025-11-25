这份指南基于谷歌官方最新的 Gemini API 文档（`google-genai` SDK）编写。它将带你从零开始，掌握从基础文本生成到高级多模态、Agent 构建及函数调用的所有核心技能。

**前置准备：**
确保你已安装 Python SDK：
```bash
pip install google-genai
```
并拥有 API Key。

---

# 第一章：你好，Gemini (基础入门)

一切从初始化客户端和最简单的文本生成开始。这是所有后续操作的基石。

### 1.1 初始化与首次调用
新的 Python SDK 使用 `google.genai` 模块。

```python
from google import genai

# 1. 初始化客户端
client = genai.Client(api_key="YOUR_API_KEY") 
# 注意：如果设置了环境变量 GEMINI_API_KEY，可直接 client = genai.Client()

# 2. 调用模型生成内容
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="用简练的语言解释人工智能是如何工作的",
)

# 3. 打印结果
print(response.text)
```

### 1.2 认识模型家族
在开发前，你需要知道选哪个模型：

*   **Gemini 3 Pro (Preview):** 最智能的模型，拥有世界级的多模态理解力，支持高级推理和 Agent 任务。**注意：建议保持 Temperature 为 1.0。**
*   **Gemini 2.5 Pro:** 强大的推理模型，擅长编程和复杂任务。
*   **Gemini 2.5 Flash:** 性价比之王，平衡了速度与智能，100万 Token 上下文。
*   **Gemini 2.5 Flash-Lite:** 极速、低成本，适合高频任务。
*   **Gemini 2.0 Flash:** 上一代的主力模型。

---

# 第二章：视觉与多模态 (Vision)

Gemini 是原生的多模态模型。你可以输入图片、PDF、视频等。

### 2.1 传入本地图片 (Inline Data)
对于小于 20MB 的请求，可以直接以内联方式传输图片数据。

```python
from google import genai
from google.genai import types

client = genai.Client()

# 读取本地文件
with open('path/to/image.jpg', 'rb') as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        '给这张图片写个标题。'
    ]
)
print(response.text)
```

### 2.2 传入网络图片
你可以使用 `requests` 库获取图片并转换。

```python
import requests
from google import genai
from google.genai import types

image_url = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_url).content

# 转换为 Part 对象
image_part = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=["这也是什么乐器？", image_part],
)
print(response.text)
```

### 2.3 File API (处理大文件)
对于大文件或需要重复使用的文件，建议使用 File API 上传。

```python
# 1. 上传文件
my_file = client.files.upload(file="path/to/large_image.jpg")

# 2. 在生成中使用文件引用
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[my_file, "这张图里有什么细节？"],
)
print(response.text)
```

### 2.4 高级视觉能力：物体检测 (Object Detection)
Gemini 2.0 及以上版本支持检测物体并返回边界框（Bounding Box）。
**关键点：** 坐标是归一化的 `[ymin, xmin, ymax, xmax]`，范围是 0-1000。你需要根据原图尺寸进行换算。

```python
from PIL import Image
import json

prompt = "检测图中所有主要物品。返回 box_2d 格式为 [ymin, xmin, ymax, xmax]，范围0-1000。"
image = Image.open("path/to/image.png")

config = types.GenerateContentConfig(response_mime_type="application/json")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[image, prompt],
    config=config
)

# 解析坐标并换算
width, height = image.size
bounding_boxes = json.loads(response.text)

for item in bounding_boxes:
    box = item["box_2d"]
    # 换算回像素坐标
    abs_y1 = int(box[0]/1000 * height)
    abs_x1 = int(box[1]/1000 * width)
    abs_y2 = int(box[2]/1000 * height)
    abs_x2 = int(box[3]/1000 * width)
    print(f"物体位置: {abs_x1}, {abs_y1}, {abs_x2}, {abs_y2}")
```

### 2.5 高级视觉能力：图像分割 (Segmentation)
Gemini 2.5 支持生成分割掩码（Mask）。
**关键技巧：** 为了获得更好的结果，需要将 `thinking_budget` 设置为 0。

```python
import base64
import io
import numpy as np
from PIL import Image

# 配置 Thinking Budget 为 0
config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_budget=0) 
)

prompt = """
给出木制和玻璃物品的分割掩码。
输出JSON列表，包含 "box_2d", "mask" (base64 png), "label"。
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[prompt, image],
    config=config
)

items = json.loads(response.text) # 解析 JSON (需处理 Markdown 代码块)

for item in items:
    # 处理掩码
    png_str = item["mask"].removeprefix("data:image/png;base64,")
    mask_data = base64.b64decode(png_str)
    mask = Image.open(io.BytesIO(mask_data))
    # 注意：Mask 需要调整大小以匹配 Bounding Box 的尺寸
    print(f"获取到 {item['label']} 的掩码")
```

---

# 第三章：结构化输出 (Structured Outputs)

让模型不再输出“废话”，而是严格符合格式的 JSON 数据。这对程序化集成至关重要。

### 3.1 使用 Pydantic 定义 Schema
SDK 支持直接传入 Pydantic 模型来定义 JSON Schema。

```python
from pydantic import BaseModel, Field
from typing import List, Optional

# 1. 定义数据结构
class Ingredient(BaseModel):
    name: str = Field(description="原料名称")
    quantity: str = Field(description="数量，包含单位")

class Recipe(BaseModel):
    recipe_name: str = Field(description="食谱名称")
    prep_time_minutes: Optional[int] = Field(description="准备时间（分钟）")
    ingredients: List[Ingredient]
    instructions: List[str]

# 2. 发送请求并配置 Schema
prompt = "提取这个食谱：想要做巧克力曲奇，需要2又1/4杯面粉，1茶匙苏打..."

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": Recipe.model_json_schema(),
    },
)

# 3. 验证并转为对象
recipe = Recipe.model_validate_json(response.text)
print(recipe.recipe_name)
print(recipe.ingredients[0].name)
```

### 3.2 结构化输出与工具结合 (Gemini 3 Preview)
Gemini 3 可以在使用工具（如搜索）的同时，强制输出结构化数据。

```python
# 定义你想要的比赛结果结构
class MatchResult(BaseModel):
    winner: str
    score: str

response = client.models.generate_content(
    model="gemini-3-pro-preview",
    contents="搜索最新的欧洲杯详细信息",
    config={
        "tools": [{"google_search": {}}], # 启用搜索工具
        "response_mime_type": "application/json",
        "response_json_schema": MatchResult.model_json_schema(), # 强制 JSON 输出
    },  
)
# 结果将是基于搜索结果生成的 JSON
```

---

# 第四章：工具使用 (Tools) & Grounding

扩展模型的能力，使其能联网、执行代码或读取特定网址。

### 4.1 谷歌搜索 (Grounding with Google Search)
让模型基于实时网络信息回答，并提供引用。

```python
from google.genai import types

# 启用搜索工具
config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="谁赢得了2024年欧洲杯？",
    config=config,
)

# 获取回答
print(response.text)

# 获取引用元数据 (Grounding Metadata)
grounding_info = response.candidates[0].grounding_metadata
print(grounding_info.search_entry_point.rendered_content) # 搜索建议 HTML
for chunk in grounding_info.grounding_chunks:
    print(chunk.web.uri) # 来源链接
```

### 4.2 代码执行 (Code Execution)
模型可以编写并运行 Python 代码来解决数学或数据处理问题。

```python
prompt = "计算斐波那契数列的前20项，然后计算它们的总和。"

config = types.GenerateContentConfig(
    tools=[{"code_execution": {}}] 
)

# 模型会自动生成代码 -> 在沙箱运行 -> 返回结果 -> 生成最终回答
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config=config
)
print(response.text)
```

### 4.3 URL Context
让模型读取特定 URL 的内容（支持 HTML, PDF 等）。

```python
url1 = "https://www.example.com/recipe1"
url2 = "https://www.example.com/recipe2"

# 启用 URL Context 工具
tools = [{"url_context": {}}]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"比较这两个网址里的食谱成分：{url1} 和 {url2}",
    config=types.GenerateContentConfig(tools=tools)
)

print(response.text)
# 查看检索状态
print(response.candidates[0].url_context_metadata)
```

---

# 第五章：函数调用 (Function Calling)

这是连接模型与你自己业务系统的桥梁。你可以定义 Python 函数，模型会决定何时调用它们。

### 5.1 自动函数调用 (Python SDK 独有神器)
Python SDK 可以直接将你的函数转换为工具，并自动处理调用循环。

```python
# 1. 定义你的实际业务函数 (必须包含类型提示和 Docstring)
def get_weather(location: str) -> dict:
    """获取指定地点的当前天气。
    
    Args:
        location: 城市名称，例如 Beijing
    """
    # 这里写实际 API 调用逻辑
    return {"temp": 25, "unit": "C", "condition": "Sunny"}

def set_light(brightness: int, color: str):
    """设置灯光亮度和颜色。"""
    return {"status": "success"}

# 2. 配置工具
tools = [get_weather, set_light] # 直接传入函数列表

# 3. 创建对话或生成内容
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(tools=tools) # 默认开启自动调用
)

# 4. 发送指令
response = chat.send_message("北京今天天气怎么样？如果是晴天就把灯调成暖色且亮度50。")

# SDK 会自动：
# 1. 调用 get_weather("Beijing")
# 2. 拿到结果 "Sunny"
# 3. 再次调用 set_light(50, "warm")
# 4. 生成最终回复
print(response.text) 
```

### 5.2 组合式与并行函数调用
上面的例子展示了**组合式调用**（先查天气，再调灯光）。Gemini 也支持**并行调用**（Parallel Function Calling），例如：
`"帮我查一下上海和东京的天气"` -> 模型会同时发出两个 `get_weather` 请求。

### 5.3 控制函数调用模式 (Modes)
你可以强制模型必须使用工具，或者禁止使用。

```python
# 强制模型必须调用 'get_weather'
tool_config = types.ToolConfig(
    function_calling_config=types.FunctionCallingConfig(
        mode="ANY", # ANY: 强制调用; AUTO: 自动决定; NONE: 禁用
        allowed_function_names=["get_weather"]
    )
)
```

### 5.4 模型上下文协议 (MCP)
SDK 内置支持 MCP。如果你有运行中的 MCP 服务器，可以直接连接。

```python
# 需安装 mcp: pip install mcp
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# ... 连接 MCP Server 代码 ...
# 在 generate_content 配置中：
# tools=[session] 
# SDK 会自动处理 MCP 工具调用
```

---

# 第六章：提示词工程 (Prompt Design)

掌握如何更好地向模型提问。

### 6.1 核心策略
1.  **清晰具体：** 给出指令、上下文、约束。
2.  **Few-shot (少样本)：** 提供 1-3 个示例比单纯描述指令更有效。
    *   *示例：*
        `文本: 犀牛 -> 类别: 大型`
        `文本: 老鼠 -> 类别: 小型`
        `文本: 大象 -> 类别: `
3.  **格式控制：** "请输出 JSON" 或 "请使用 Markdown 列表"。
4.  **思维链 (CoT):** 即使不使用思考模型，让模型 "一步步思考" 也能提高准确率。

### 6.2 Gemini 3 特别指南
Gemini 3 擅长推理，但也更敏感。
*   **Temperature:** 强烈建议保持为 `1.0`。调低可能会导致死循环或性能下降。
*   **XML 标签:** 使用 `<task>`, `<context>`, `<constraints>` 标签来组织复杂的 Prompt，Gemini 3 对这种结构理解得非常好。
*   **明确规划:** 对于复杂任务，指示模型：“在回答前，先制定计划”。

### 6.3 思考模型 (Thinking Models)
Gemini 3 和 2.5 系列拥有内部思考过程。
如果你手动管理对话历史（非 SDK 自动模式），必须保留并传回 `thought_signature`，否则会丢失思考上下文。

---

# 第七章：构建 Agent (LangGraph)

Gemini 与 LangGraph 完美集成，适合构建复杂的 ReAct Agent。

```python
# 需要安装: pip install langgraph langchain-google-genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END
# ... 定义工具和状态 ...

# 创建 LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    google_api_key=api_key
)

# 绑定工具
model = llm.bind_tools(tools)

# 构建 Graph (Nodes & Edges)
workflow = StateGraph(AgentState)
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)
# ... 设置边 ...
app = workflow.compile()
```
*注：LangGraph 是构建有状态、多步骤 Agent 的推荐框架。*

---

# 总结：学习路径

1.  **入门：** 熟练使用 `client.models.generate_content` 进行文本对话。
2.  **进阶：** 尝试传入图片、PDF，体验 Gemini 2.5 Flash 的多模态能力。
3.  **工程化：** 使用 `response_json_schema` 获得结构化数据，这对开发 App 至关重要。
4.  **连接世界：** 开启 `google_search` 工具增强事实准确性。
5.  **业务集成：** 使用 Python SDK 的**自动函数调用**功能，将你现有的 Python 代码接入 AI。
6.  **大师级：** 使用 Gemini 3 Pro，配合精心设计的 XML Prompt 和 LangGraph 构建自主 Agent。