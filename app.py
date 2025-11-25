import gradio as gr
from google import genai
# 【V16 修复】严格按照文档和您的指示，导入 types
from google.genai import types as genai_types
from pydantic import BaseModel, Field, ValidationError, TypeAdapter
from typing import List, Optional
import os
import time
import json
from PIL import Image
import numpy as np # 确保导入 numpy

# --- 1. UI/UX 增强: 自定义CSS与品牌元素 ---
GEMINI_LOGO_SVG = """<svg width="30px" height="30px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="display: inline-block; vertical-align: middle; margin-right: 8px;"><path d="M12 21.5C12 21.5 11.5 18.5 12 15.5C12.5 12.5 15 11.5 18 11.5C21 11.5 21.5 14 21.5 15.5C21.5 17 21.5 21.5 21.5 21.5C21.5 21.5 17.5 21.5 12 21.5Z" fill="url(#paint0_linear_10_23)"></path><path d="M2.5 12C2.5 12 5.5 11.5 8.5 12C11.5 12.5 12.5 15 12.5 18C12.5 21 10 21.5 8.5 21.5C7 21.5 2.5 21.5 2.5 21.5C2.5 21.5 2.5 17.5 2.5 12Z" fill="url(#paint1_linear_10_23)"></path><path d="M8.5 2.5C8.5 2.5 11 3 12 6C13 9 11.5 10 8.5 10C5.5 10 2.5 9.5 2.5 8C2.5 6.5 2.5 2.5 2.5 2.5C2.5 2.5 4 2.5 8.5 2.5Z" fill="url(#paint2_linear_10_23)"></path><defs><linearGradient id="paint0_linear_10_23" x1="12" y1="11.5" x2="21.5" y2="21.5" gradientUnits="userSpaceOnUse"><stop stop-color="#89B5F7"></stop><stop offset="1" stop-color="#4285F4"></stop></linearGradient><linearGradient id="paint1_linear_10_23" x1="2.5" y1="12" x2="12.5" y2="21.5" gradientUnits="userSpaceOnUse"><stop stop-color="#FCD26A"></stop><stop offset="1" stop-color="#FABB05"></stop></linearGradient><linearGradient id="paint2_linear_10_23" x1="2.5" y1="2.5" x2="12" y2="10" gradientUnits="userSpaceOnUse"><stop stop-color="#85E29A"></stop><stop offset="1" stop-color="#34A853"></stop></linearGradient></defs></svg>"""

APP_CSS = """
<style>
@keyframes gemini-gradient { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }
.gemini-title { font-size: 2.5em !important; font-weight: bold; background: linear-gradient(to right, #4285F4, #DB4437, #F4B400, #0F9D58, #4285F4); -webkit-background-clip: text; background-clip: text; color: transparent; background-size: 200% auto; animation: gemini-gradient 5s ease-in-out infinite; margin: 0; }
.log-panel .gradio-textbox { border: 2px solid #444; background-color: #1a1a1a; color: #00ff99; font-family: 'Courier New', Courier, monospace; }
</style>
"""

# --- 客户端初始化 ---
# 文档引用: "提交第一个请求"
# from google import genai
# client = genai.Client()
try:
    client = genai.Client()
except Exception as e:
    client = None

# --- 2. Pydantic Schema 定义 (用于初始检测) ---
# 文档引用: "生成 JSON"
# from pydantic import BaseModel
class ImageContext(BaseModel):
    is_relevant: bool
    scene_chinese: str
    reasoning: str

class BoundingBox(BaseModel):
    y_min: int
    x_min: int
    y_max: int
    x_max: int

class DetectedItem(BaseModel):
    label: str
    description: str
    confidence: float
    box_2d: BoundingBox
    suggested_tags: Optional[List[str]] = Field(default_factory=list)

# --- 3. 核心后端逻辑 ---

# 【V20 修复】
def call_gemini_api(model, prompt, image, pydantic_type):
    """
    (用于初始分析) 单轮API调用，返回结构化 Pydantic 对象。
    【V20 修复】: 还原为使用 TypeAdapter 手动生成 JSON Schema，
    以解决 `Unsupported schema type: ... type=None` 错误。
    """
    if not client: return {"error": "Gemini Client未初始化。"}
    try:
        # 1. 【关键修复】使用 TypeAdapter 手动创建 JSON Schema 字典。
        #    这是您最初代码中的做法，也是最健壮的方法。
        adapter = TypeAdapter(pydantic_type)
        schema_dict = adapter.json_schema()

        # 2. 严格遵循 "结构化输出" -> "生成 JSON" 文档，
        #    传递一个 *包含* "response_schema" 键的 Python 字典。
        config_dict = {
            "response_mime_type": "application/json",
            "response_schema": schema_dict # <-- 传递生成的字典，而不是类型
        }

        # 3. 文档引用: "提交第一个请求" -> client.models.generate_content(...)
        response = client.models.generate_content(
            model=model, 
            contents=[image, prompt], # <-- 合法的 [Image, str] 格式
            config=config_dict # <-- 传递包含 schema 字典的 config
        )
        
        # 4. 【关键修复】使用 TypeAdapter 解析 JSON 文本。
        #    文档指出 .parsed 可能会静默失败。
        #    您最初的 `adapter.validate_json` 方法更健壮。
        return adapter.validate_json(response.text)
    
    except Exception as e:
        # 将 Pydantic 验证错误暴露给日志
        print(f"[call_gemini_api FAILED] Model: {model}, Error: {str(e)}")
        return {"error": f"API调用失败: {str(e)}"}


def process_image(uploaded_image):
    """
    处理图像上传，运行分诊，检测，并【创建和启动】一个新的聊天会话。
    """
    if uploaded_image is None:
        # (输出: log, image, analysis_state, scene_state, chat_panel, chatbot_ui, chat_session_state)
        yield "请先上传一张图片。", None, [], "", gr.update(visible=False), [], None
        return

    pil_image = Image.fromarray(uploaded_image).convert("RGB")
    log_text = "初始化分析流程...\n"
    yield log_text, (pil_image, []), [], "", gr.update(visible=False), [], None

    # --- 阶段 1: 分诊 (结构化输出) ---
    log_text += "----------\n[阶段 1/2] 调用 Gemini 2.5 Flash 进行课题相关性分诊...\n"
    yield log_text, (pil_image, []), [], "", gr.update(visible=False), [], None
    
    triage_prompt = """
    你是一位严格的AI助教，负责评审一篇本科毕业设计。
    课题名称：《基于社交媒体数据的用户健康画像构建》。
    核心目标：通过分析用户在社交媒体上发布的图片，推断其健康和生活方式。
    你的任务：判断当前上传的这张图片是否符合该课题的研究范围。
    
    符合标准的图片应具备以下特征：
    1.  **真实生活场景**: 必须是真实拍摄的、与个人生活直接相关的照片。
    2.  **可推断性**: 图片内容能明确或间接地反映出以下至少一种信息：
        - **饮食习惯**: 拍摄了正餐、零食、饮料等。
        - **运动状态**: 健身房打卡、户外跑步、球类运动等。
        - **作息模式**: 能看出是清晨或深夜的活动，例如深夜在电脑前工作（可推断为'熬夜'）。
        - **社交活动**: 聚会、饮酒等场景。
        - **情绪暗示**: 整体环境或人物状态能暗示情绪。

    不符合标准的图片包括：
    - 纯风景照、网络梗图、动漫截图、屏幕录屏、抽象艺术品、广告宣传图等。

    请严格按照指定的JSON格式，用中文返回你的评审结果。
    """
    # 【V16】调用已修复的 call_gemini_api
    triage_result = call_gemini_api('gemini-2.5-flash', triage_prompt, pil_image, ImageContext)

    if isinstance(triage_result, dict) or not hasattr(triage_result, 'is_relevant') or not triage_result.is_relevant:
        reason = triage_result.reasoning if hasattr(triage_result, 'reasoning') else triage_result.get('error', '未知错误')
        log_text += f"❌ 分诊【不通过】。\n评审理由: {reason}\n流程终止。"
        yield log_text, (pil_image, []), [], "", gr.update(visible=False), [], None
        return
    
    log_text += f"✅ 分诊【通过】！\n场景判断: {triage_result.scene_chinese}\n"
    yield log_text, (pil_image, []), [], triage_result.scene_chinese, gr.update(visible=False), [], None
    time.sleep(1)

    # --- 阶段 2: 深度分析 (结构化输出) ---
    log_text += "----------\n[阶段 2/2] 调用 Gemini 2.5 Pro 进行深度分析与标注...\n"
    yield log_text, (pil_image, []), [], triage_result.scene_chinese, gr.update(visible=False), [], None

    detection_prompt = f"""
    你是一位资深的健康数据分析师，正在为一个名为《基于社交媒体数据的用户健康画像构建》的毕业设计项目工作。
    已知当前图片场景是关于“{triage_result.scene_chinese}”。
    你的核心任务是：从这张图片中**榨取所有与个人健康、情绪、和行为模式相关的信号**，而不仅仅是识别物体。

    请遵循以下严格指令：
    1.  **全面检测**: 详细检测图中的所有关键元素。
    2.  **情景化标签**: 标签(label)不仅要说明物体是什么，更要体现其在健康画像中的意义。例如，一碗米饭是“饮食-主食”，一个哑铃是“运动-器械”，深夜的电脑是“作息-熬夜迹象”。
    3.  **深度描述**: 描述(description)需要简要分析该元素对健康画像的潜在贡献。
    4.  **智能推断标签 (Suggested Tags)**:
        - 如果置信度高（>0.9），并且可以明确推断出一种健康相关的状态（例如深夜的电脑屏幕可推断为'熬夜'，一杯酒可推断为'饮酒'），请在`suggested_tags`中提供这一个确定的状态标签。
        - 如果置信度低（<=0.9），或者物体有多种可能性，请在`suggested_tags`中提供2-3个最有可能的中文候选标签。
    5.  **严格格式**: 你的回答必须是严格遵循Schema的JSON对象列表。
    """
    # 【V16】调用已修复的 call_gemini_api，传递 List[DetectedItem] 类型
    detection_result = call_gemini_api('gemini-2.5-pro', detection_prompt, pil_image, List[DetectedItem])

    if isinstance(detection_result, dict) or not detection_result:
        error_msg = detection_result.get('error', '未能检测到任何物体。')
        log_text += f"❌ 深度分析失败。\n理由: {error_msg}\n流程终止。"
        yield log_text, (pil_image, []), [], triage_result.scene_chinese, gr.update(visible=False), [], None
        return
        
    log_text += f"✅ 深度分析成功！共识别出 {len(detection_result)} 个关键元素。\n----------\n分析全部完成。"

    # --- 阶段 3: 创建并启动聊天会话 (V15 架构) ---
    
    # 1. (不变) 生成标注
    annotations = []
    w, h = pil_image.size
    for i, item in enumerate(detection_result):
        box = item.box_2d
        label_text = f"[{i}] {item.label}"
        if item.suggested_tags: label_text += f" ({', '.join(item.suggested_tags)})"
        annotation_box = (int(box.x_min/1000*w), int(box.y_min/1000*h), int(box.x_max/1000*w), int(box.y_max/1000*h))
        annotations.append((annotation_box, label_text))
    final_annotated_image = (pil_image, annotations)
    
    # 2. (不变) 准备 *UI* 的第一条消息
    initial_summary = f"分析完成！我判断这是一个**{triage_result.scene_chinese}**的场景。图片上的标签是我检测到的关键元素 (已编号)，您可以点击任意一个与我互动。"
    initial_chatbot_history = [{"role": "assistant", "content": initial_summary}]

    try:
        # 3. 创建聊天会话
        # 文档引用: "多轮对话（聊天）" -> chat = client.chats.create(...)
        chat_session = client.chats.create(model="gemini-2.5-flash")
        
        # 4. 准备“虚拟第0轮”的统一提示（图像 + 标签列表）
        all_labels_summary = "\n".join([
            f"  - [{i}] {item.label}: {item.description}" 
            for i, item in enumerate(detection_result)
        ])
        unified_text_prompt = f"""
        这是我上传的图片。请你以这张图片为唯一的、完整的上下文。之后我所有的对话（包括点击标签）都是关于这张图的。请基于全图进行分析和回复。

        【系统初始上下文】
        你已经分析了这张图，这是你的分析结果：
        - **整体场景判断:** {triage_result.scene_chinese}
        - **检测到的关键元素列表 (索引, 标签, 描述):**
{all_labels_summary}

        请牢记这个列表。用户接下来的所有互动（无论是点击还是聊天）都将基于这张图和这个列表。请回复“收到”以确认。
        """
        
        # 5. "启动"会话：发送图像和上下文作为第一条消息
        # 文档引用: "多轮对话（聊天）" -> chat.send_message(...)
        # 文档引用: "多模态输入" -> contents=[image, "Tell me about this instrument"]
        #    (chat.send_message 是 generate_content 的封装器，支持此 [Image, str] 格式)
        priming_response = chat_session.send_message([pil_image, unified_text_prompt])
        log_text += f"\n[V16] 聊天会话已启动。AI 启动回复: {priming_response.text}"
        
        # 6. 成功，返回所有状态
        yield (
            log_text, 
            final_annotated_image, 
            detection_result, 
            triage_result.scene_chinese, 
            gr.update(visible=True), 
            initial_chatbot_history,
            chat_session # <-- 【V15】输出有状态的聊天对象
        )
        
    except Exception as e:
        log_text += f"\n❌ [V16] 聊天会话启动失败: {e}"
        yield (
            log_text, 
            final_annotated_image, 
            detection_result, 
            triage_result.scene_chinese, 
            gr.update(visible=True), 
            initial_chatbot_history, # UI 仍然显示
            None # 聊天会话失败
        )


def _regenerate_annotations(original_numpy_image, analysis_result_list: List[DetectedItem]):
    """(不变) 辅助函数：从Numpy图像和结果列表重新生成带索引的标注"""
    if original_numpy_image is None: return None
    original_image_pil = Image.fromarray(original_numpy_image).convert("RGB")
    w, h = original_image_pil.size
    new_annotations = []
    for i, item in enumerate(analysis_result_list):
        box = item.box_2d; label_text = f"[{i}] {item.label}"
        if item.suggested_tags: label_text += f" ({', '.join(item.suggested_tags)})"
        annotation_box = (int(box.x_min/1000*w), int(box.y_min/1000*h), int(box.x_max/1000*w), int(box.y_max/1000*h))
        new_annotations.append((annotation_box, label_text))
    return (original_image_pil, new_annotations)


def handle_select(state_analysis_result: List[DetectedItem], 
                  chat_history: list, 
                  state_chat_session, # <-- 【V18 修复】移除类型提示
                  evt: gr.SelectData):
    """
    【已重构 v16 - 使用 Chat API】
    处理用户点击标签事件的函数。
    """

    if state_chat_session is None:
        chat_history.append({"role": "assistant", "content": "抱歉，聊天会话未初始化，请重新上传图片。"})
        return chat_history, None, state_chat_session # 返回 None chat_session

    output_selected_object = None # 默认不改变
    
    # (V4 修复) 忽略非标注框点击
    if evt.index is None:
        print(f"Ignored select event: No index provided (e.g., title click). Value was: {evt.value}")
        return chat_history, None, state_chat_session
    
    try:
        selected_index = evt.index
        
        if 0 <= selected_index < len(state_analysis_result):
            selected_object = state_analysis_result[selected_index]
            
            # 1. 准备用户消息 和 系统指令
            user_click_message = f"（我点击了标签 [{selected_index}]: “{selected_object.label}”）"
            system_prompt_for_click = f"""
            你是一个富有同理心且洞察力敏锐的智能助手。
            【上下文】你已经看到了完整的图片和所有检测元素的列表。
            【用户操作】用户刚刚在图片上点击了 编号为 [{selected_index}] 的物体“{selected_object.label}”（基础描述：“{selected_object.description}”）。
            【你的任务】请结合**整张图片**的上下文（不仅仅是标签，利用你看到的全图）和**完整的检测列表**，主动推测用户可能关心的问题，或者给出一个有趣的、相关的洞察。你的回复要自然、友好，像是在开启一段对话。
            """
            
            # 2. 将用户消息和系统指令合并为 *一个* 字符串
            final_user_prompt = f"{user_click_message}\n\n{system_prompt_for_click}"

            # 3. 更新 UI (显示用户点击 + 加载)
            chat_history.append({"role": "user", "content": user_click_message})
            chat_history.append({"role": "assistant", "content": "🤔 正 在 为 您 分 析..."})

            # 4. 调用 Chat API
            # 文档引用: "多轮对话（聊天）" -> response = chat.send_message("How many paws...")
            response = state_chat_session.send_message(final_user_prompt) # <-- 发送 [str]
            
            # 5. 更新 UI
            chat_history[-1] = {"role": "assistant", "content": response.text}
            output_selected_object = {"index": selected_index, "data": selected_object.model_dump()}
        else:
            print(f"Error: evt.index {selected_index} is out of bounds.")
            chat_history.append({"role": "assistant", "content": f"抱歉，我内部好像出错了，找不到索引 {selected_index}。"})
            
    except Exception as e:
        print(f"Error in handle_select logic: {e}")
        error_message = f"抱歉，处理点击时出错: {str(e)}"
        if chat_history and chat_history[-1]["role"] == "assistant":
             chat_history[-1] = {"role": "assistant", "content": error_message}
        else:
            chat_history.append({"role": "assistant", "content": error_message})

    # 返回 UI 更新, 并将 *同一个* chat_session 对象传回 state
    return chat_history, output_selected_object, state_chat_session


def handle_reply(state_analysis_result: List[DetectedItem], 
                 state_selected_object: dict, 
                 user_input: str, 
                 chat_history: list, 
                 original_numpy_image: np.ndarray,
                 state_chat_session): # <-- 【V18 修复】移除类型提示
    """
    【已重构 v16 - 使用 Chat API】
    处理用户的文本回复。
    """
    
    
    # (V2 修复) 处理空输入
    if not user_input:
        current_annotated_image = _regenerate_annotations(original_numpy_image, state_analysis_result)
        # (chat_history, chat_input, annotated_output, analysis_result, chat_session)
        return chat_history, "", current_annotated_image, state_analysis_result, state_chat_session

    if state_chat_session is None:
        chat_history.append({"role": "assistant", "content": "抱歉，聊天会话未初始化，请重新上传图片。"})
        current_annotated_image = _regenerate_annotations(original_numpy_image, state_analysis_result)
        return chat_history, "", current_annotated_image, state_analysis_result, state_chat_session

    # 1. 准备系统指令
    selected_object_context = f"用户当前正在讨论的物体是 编号[{state_selected_object['index']}] '{state_selected_object['data']['label']}'。" if state_selected_object else ""
    system_prompt_for_reply = f"""
    你是一个智能助手。
    【重要上下文】你**能看到整张图片**，并且你**已经有了一个完整的检测元素列表**（在历史记录的开头）。请始终结合**全图上下文**、**完整的检测列表**、{selected_object_context} 和对话历史来回答。
    
    【用户最新回复】: "{user_input}"

    你的任务是:
    1.  **继续对话**: 生成一段自然的、有帮助的回复。
    2.  **识别修正意图**: 如果用户的回复明确指出了一个识别错误（例如“那不是XX，是YY”），你必须在你的对话回复之后，另起一行，嵌入一个特定格式的JSON指令块来修正标签。
    3.  **返回索引**: 你的JSON必须包含被修正物体的数字索引 `index`。

    JSON指令格式: `ACTION_JSON:{{"action": "update_label", "index": <被修正物体的数字编号>, "new_label": "用户提供的新标签"}}`
    """
    
    # 2. 将用户 *实际输入* 和系统指令合并为 *一个* 字符串
    final_user_prompt = f"{user_input}\n\n{system_prompt_for_reply}"
    
    # 3. 更新 UI (显示用户输入 + 加载)
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": "🤔 正 在 为 您 分 析..."})
    
    try:
        # 4. 调用 Chat API
        # 文档引用: "多轮对话（聊天）" -> response = chat.send_message("How many paws...")
        response = state_chat_session.send_message(final_user_prompt) # <-- 发送 [str]
        full_response_text = response.text
        
        # 5. 更新 UI (仅对话部分)
        chat_history[-1] = {"role": "assistant", "content": full_response_text.split("ACTION_JSON:")[0].strip()}
        
        # (不变) 处理 ACTION_JSON 的逻辑
        new_analysis_result = state_analysis_result
        if "ACTION_JSON:" in full_response_text:
            try:
                action_str = full_response_text.split("ACTION_JSON:")[1]
                action_data = json.loads(action_str)
                
                if action_data.get("action") == "update_label":
                    target_index = int(action_data['index'])
                    new_label = action_data['new_label']
                    
                    if 0 <= target_index < len(state_analysis_result):
                        truly_new_list = list(state_analysis_result) 
                        updated_item = truly_new_list[target_index].model_copy(
                            update={'label': new_label, 'suggested_tags': []} 
                        )
                        truly_new_list[target_index] = updated_item
                        new_analysis_result = truly_new_list
                    else:
                        print(f"AI返回的索引 {target_index} 超出范围。")
                        
            except Exception as e:
                print(f"解析或执行Action指令失败: {e}")

        # (不变) 重新生成标注
        new_annotated_image = _regenerate_annotations(original_numpy_image, new_analysis_result)
                
        return chat_history, "", new_annotated_image, new_analysis_result, state_chat_session
        
    except Exception as e:
        # 捕获 API 错误
        print(f"Error in handle_reply logic: {e}")
        error_message = f"抱歉，处理回复时出错: {str(e)}"
        chat_history[-1] = {"role": "assistant", "content": error_message}
        # Gradio 错误修复：保持图像和状态不变
        current_annotated_image = _regenerate_annotations(original_numpy_image, state_analysis_result)
        return chat_history, "", current_annotated_image, state_analysis_result, state_chat_session


# --- 5. 构建 Gradio Web 界面 ---
with gr.Blocks(theme='gradio/dracula_revamped') as demo:
    gr.HTML(APP_CSS)
    gr.HTML(f'<div style="display: flex; align-items: center;">{GEMINI_LOGO_SVG}<h1 class="gemini-title">动态健康孪生智能体 v16.0 </h1></div>')
    
    # 状态：存储Pydantic对象列表 List[DetectedItem]
    state_analysis_result = gr.State([])
    # 状态：存储场景字符串
    state_scene = gr.State("")
    # 状态：存储被选中对象的信息 {"index": int, "data": dict}
    state_selected_object = gr.State(None)
    # 【V15】存储有状态的 chat SDK 对象
    state_chat_session = gr.State(None) 

    with gr.Row():
        with gr.Column(scale=3):
            # image_input (Numpy) 是我们统一上下文的图像源
            image_input = gr.Image(type="numpy", label="上传您的生活照片")
            submit_btn = gr.Button("开始分析", variant="primary")
            annotated_output = gr.AnnotatedImage(label="分析结果（点击带编号的标签互动）", height=400)

        with gr.Column(scale=2):
            log_box = gr.Textbox(label="⚙️ 完整技术日志", lines=15, interactive=False, elem_classes=["log-panel"])
            with gr.Group(visible=False) as interaction_panel:
                chatbot = gr.Chatbot(label="智能交互区 (已连接 Chat API)", height=350, type="messages", avatar_images=("user.png", "gemini.png"))
                with gr.Row():
                    chat_input = gr.Textbox(show_label=False, scale=9, interactive=True, placeholder="输入您的回复或修正...")
                    chat_submit_btn = gr.Button("发送", variant="primary", scale=1)

    # 事件绑定
    submit_btn.click(
        fn=process_image,
        inputs=[image_input],
        outputs=[
            log_box, 
            annotated_output, 
            state_analysis_result, 
            state_scene, 
            interaction_panel, 
            chatbot,
            state_chat_session # <-- 【V15 绑定】
        ]
    )
    
    annotated_output.select(
        fn=handle_select,
        inputs=[
            state_analysis_result, 
            chatbot, 
            state_chat_session, # <-- 【V15 绑定】
        ],
        outputs=[
            chatbot, 
            state_selected_object,
            state_chat_session # <-- 【V15 绑定】
        ]
    )

    chat_submit_btn.click(
        fn=handle_reply,
        inputs=[
            state_analysis_result, 
            state_selected_object, 
            chat_input, 
            chatbot, 
            image_input, # <-- _regenerate_annotations 仍需要它
            state_chat_session # <-- 【V15 绑定】
        ],
        outputs=[
            chatbot, 
            chat_input, 
            annotated_output, 
            state_analysis_result,
            state_chat_session # <-- 【V15 绑定】
        ]
    )

if __name__ == "__main__":
    if client:
        # 确保头像文件存在
        if not os.path.exists("user.png"): Image.new('RGB', (100, 100), color = 'dodgerblue').save('user.png')
        if not os.path.exists("gemini.png"): Image.new('RGB', (100, 100), color = '#7e57c2').save('gemini.png')
        demo.launch(share=True, debug=True)
    else:
        print("\n应用无法启动，请检查环境变量。")