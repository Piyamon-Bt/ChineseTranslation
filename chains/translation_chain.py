# from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from chains.llm_chain import get_llm

# def build_translation_chain():

#     template = """
# 参考术语:
# {context}

# 请将以下中文翻译成泰文:
# {text}
# """

#     prompt = PromptTemplate(
#         input_variables=["context", "text"],
#         template=template
#     )

#     llm = get_llm()

#     return LLMChain(llm=llm, prompt=prompt)
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from chains.llm_chain import get_llm


def build_translation_chain():

    template = """
参考术语:
{context}

请将以下中文翻译成泰文:
{text}
"""

    prompt = PromptTemplate(
        input_variables=["context", "text"],
        template=template
    )

    llm = get_llm()

    # LCEL style
    chain = prompt | llm | StrOutputParser()

    return chain