from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from chains.llm_chain import get_llm


def build_analysis_chain():

    template = """
请分析以下泰文内容:
1. 总结
2. 提取关键点

{text}
"""

    prompt = PromptTemplate(
        input_variables=["text"],
        template=template
    )

    llm = get_llm()

    # ใช้ LCEL แทน LLMChain
    chain = prompt | llm | StrOutputParser()

    return chain
