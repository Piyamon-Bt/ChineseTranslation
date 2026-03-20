def validate_node(state):
    length_ratio = len(state["translated_text"]) / len(state["original_text"])

    confidence = 0.85 if 0.5 < length_ratio < 2 else 0.4

    return {
        "confidence_score": confidence,
        "is_valid": confidence > 0.6
    }
