def chunk_node(state):
    text = state["original_text"]
    chunk_size = 1200

    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    return {"chunks": chunks}
