from langgraph.graph import StateGraph, END
from state import DocumentState

from nodes.extract import extract_node
from nodes.chunk import chunk_node
from nodes.classify import classify_node
from nodes.translate import translate_node
from nodes.analyze import analyze_node
from nodes.validate import validate_node

def router(state: DocumentState):
    doc_type = state.get("document_type", "")

    if "合同" in doc_type:
        return "Translate"
    else:
        return "Translate"  # ตอนนี้ยังไปทางเดียว แต่อนาคตแยกได้

def build_graph():
    workflow = StateGraph(DocumentState)

    workflow.add_node("Extract", extract_node)
    workflow.add_node("Chunk", chunk_node)
    workflow.add_node("Classify", classify_node)
    workflow.add_node("Translate", translate_node)
    workflow.add_node("Analyze", analyze_node)
    workflow.add_node("Validate", validate_node)

    workflow.set_entry_point("Extract")

    workflow.add_edge("Extract", "Chunk")
    workflow.add_edge("Chunk", "Classify")

    workflow.add_conditional_edges(
        "Classify",
        router,
        {
            "Translate": "Translate"
        }
    )

    workflow.add_edge("Translate", "Analyze")
    workflow.add_edge("Analyze", "Validate")
    workflow.add_edge("Validate", END)

    return workflow.compile()
