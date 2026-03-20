from services.llm import query_llm

def analyze_node(state):
    prompt = f"""
请分析以下泰文：
1. 总结
2. 关键点

{state["translated_text"][:2000]}
"""
    result = query_llm(prompt)

    return {"summary": result}
