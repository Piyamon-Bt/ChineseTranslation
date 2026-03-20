# from services.llm import query_llm
# from services.rag import retrieve_context

# def translate_node(state):
#     translated = []

#     for chunk in state["chunks"]:
#         context = retrieve_context(chunk)

#         prompt = f"""
# 参考术语：
# {context}

# 请翻译成泰文：
# {chunk}
# """
#         result = query_llm(prompt)
#         translated.append(result)

#     return {
#         "translated_chunks": translated,
#         "translated_text": "\n".join(translated)
#     }

from chains.translation_chain import build_translation_chain
from chains.rag_chain import build_vector_store

vector_store = build_vector_store()
translation_chain = build_translation_chain()

def translate_node(state):
    translated_chunks = []

    for chunk in state["chunks"]:
        docs = vector_store.similarity_search(chunk, k=2)
        context = "\n".join([doc.page_content for doc in docs])

        result = translation_chain.run({
            "context": context,
            "text": chunk
        })

        translated_chunks.append(result)

    return {
        "translated_chunks": translated_chunks,
        "translated_text": "\n".join(translated_chunks)
    }
