from services.llm import query_llm

def classify_node(state):
    prompt = f"""
请判断文件类型：
合同 / 技术文档 / 发票 / 研究论文 / 其他

内容：
{state["original_text"][:1000]}
"""
    result = query_llm(prompt)
    return {"document_type": result}
