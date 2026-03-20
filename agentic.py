from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional, List
import os

# =========================
# 1️⃣ Define State
# =========================

class DocumentState(TypedDict):
    # Input
    file_path: Optional[str]
    original_text: Optional[str]

    # Processing
    document_type: Optional[str]

    # Translation
    translated_text: Optional[str]

    # Analysis
    summary: Optional[str]
    key_points: Optional[List[str]]

    # Control
    is_valid: Optional[bool]
    output: Optional[str]


# =========================
# 2️⃣ Node Functions
# =========================

# Input Node
def input_node(state: DocumentState):
    if not state.get("file_path"):
        state["file_path"] = input("Enter file path: ")

    return state


# Extract Text Node (Mock version)
def extract_text_node(state: DocumentState):
    file_path = state.get("file_path")

    if not file_path or not os.path.exists(file_path):
        return {"original_text": "Sample Chinese document 内容测试合同条款付款方式。"}

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    return {"original_text": text}


# Classification Node (Mock LLM Logic)
def classify_node(state: DocumentState):
    text = state.get("original_text", "")

    if "合同" in text:
        doc_type = "Contract"
    else:
        doc_type = "General Document"

    return {"document_type": doc_type}


# Translation Node (Mock Translation)
def translate_node(state: DocumentState):
    text = state.get("original_text", "")

    translated = f"[THAI TRANSLATION]: {text}"

    return {"translated_text": translated}


# Analysis Node
def analyze_node(state: DocumentState):
    doc_type = state.get("document_type", "")
    text = state.get("translated_text", "")

    if doc_type == "Contract":
        summary = "This is a contract document."
        key_points = ["Payment terms", "Obligations", "Risk clauses"]
    else:
        summary = "General document summary."
        key_points = ["General info"]

    return {
        "summary": summary,
        "key_points": key_points
    }


# Validation Node
def validate_node(state: DocumentState):
    if state.get("translated_text"):
        return {"is_valid": True, "output": "Processing completed successfully."}
    else:
        return {"is_valid": False, "output": "Translation failed."}


# Router
def router(state: DocumentState):
    if state.get("is_valid"):
        return "success"
    else:
        return "failure"


# Success Node
def success_node(state: DocumentState):
    print("\n=== FINAL OUTPUT ===")
    print("Document Type:", state.get("document_type"))
    print("Summary:", state.get("summary"))
    print("Key Points:", state.get("key_points"))
    return state


# Failure Node
def failure_node(state: DocumentState):
    print("Process failed. Restarting...")
    return state


# =========================
# 3️⃣ Build Graph
# =========================

workflow = StateGraph(DocumentState)

workflow.add_node("Input", input_node)
workflow.add_node("Extract", extract_text_node)
workflow.add_node("Classify", classify_node)
workflow.add_node("Translate", translate_node)
workflow.add_node("Analyze", analyze_node)
workflow.add_node("Validate", validate_node)
workflow.add_node("Success", success_node)
workflow.add_node("Failure", failure_node)

workflow.set_entry_point("Input")

workflow.add_edge("Input", "Extract")
workflow.add_edge("Extract", "Classify")
workflow.add_edge("Classify", "Translate")
workflow.add_edge("Translate", "Analyze")
workflow.add_edge("Analyze", "Validate")

workflow.add_conditional_edges(
    "Validate",
    router,
    {
        "success": "Success",
        "failure": "Failure"
    }
)

workflow.add_edge("Success", END)
workflow.add_edge("Failure", END)

app = workflow.compile()

# =========================
# 4️⃣ Run
# =========================

result = app.invoke({
    "file_path": None
})

print("\nFinal State:")
print(result)
