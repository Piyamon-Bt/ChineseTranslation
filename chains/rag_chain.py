from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def build_vector_store():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    documents = [
        "付款条款 = เงื่อนไขการชำระเงิน",
        "违约责任 = ความรับผิดกรณีผิดสัญญา"
    ]

    return FAISS.from_texts(documents, embeddings)
