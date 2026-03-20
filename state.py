from typing import TypedDict, Optional, List

class DocumentState(TypedDict):
    file_path: Optional[str]
    original_text: Optional[str]

    chunks: Optional[List[str]]
    translated_chunks: Optional[List[str]]

    document_type: Optional[str]
    translated_text: Optional[str]

    summary: Optional[str]
    key_points: Optional[List[str]]

    confidence_score: Optional[float]
    processing_log: Optional[List[str]]

    is_valid: Optional[bool]
