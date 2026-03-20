from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "付款条款 = เงื่อนไขการชำระเงิน",
    "违约责任 = ความรับผิดกรณีผิดสัญญา"
]

embeddings = model.encode(documents)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

def retrieve_context(query):
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb), k=2)
    return [documents[i] for i in I[0]]
