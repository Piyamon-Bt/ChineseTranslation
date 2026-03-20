import fitz
from services.llm import query_llm
from ocr import run_ocr

def extract_node(state):
    file_path = state["file_path"]

    if file_path.endswith(".pdf"):
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return {"original_text": text}

    elif file_path.endswith(".png") or file_path.endswith(".jpg"):
        text = run_ocr(file_path)
        return {"original_text": text}

    return {"original_text": ""}


def classify_node(state):
    prompt = f"""
请判断以下文件类型：
合同 / 技术文档 / 发票 / 研究论文 / 其他

内容：
{state["original_text"][:1000]}
"""
    result = query_llm(prompt)
    return {"document_type": result}


def translate_node(state):
    prompt = f"""
请将以下中文翻译成泰文：
{state["original_text"][:2000]}
"""
    result = query_llm(prompt)
    return {"translated_text": result}


def analyze_node(state):
    prompt = f"""
请分析以下泰文内容：
1. 总结
2. 提取关键点

{state["translated_text"][:2000]}
"""
    result = query_llm(prompt)
    return {"summary": result}


def validate_node(state):
    if state.get("translated_text"):
        return {"is_valid": True}
    return {"is_valid": False}
