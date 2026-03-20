import fitz  # PyMuPDF
from paddleocr import PaddleOCR
import numpy as np
import cv2

# โหลด Model ไว้ข้างนอกฟังก์ชันเพื่อประหยัดเวลา
ocr_engine = PaddleOCR(use_angle_cls=True, lang="ch")

def extract_node(state):
    file_bytes = state.get("file_bytes")
    file_name = state.get("file_name", "")

    if not file_bytes:
        return {"original_text": "No file data provided"}

    # --- กรณี PDF ---
    if file_name.lower().endswith(".pdf"):
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        text = ""
        for page in doc:
            # ดึงข้อความออกมาแล้วลบการขึ้นบรรทัดใหม่ทิ้ง
            text += page.get_text().replace("\n", "")
        return {"original_text": text.strip()}

    # --- กรณี รูปภาพ (PNG, JPG) ---
    if file_name.lower().endswith((".png", ".jpg", ".jpeg")):
        nparr = np.frombuffer(file_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        result = ocr_engine.ocr(img)
        text = ""
        if result and result[0]:
            for line in result[0]:
                # line[1][0] คือข้อความที่แกะได้ 
                # เราจะบวกต่อกันไปเลยโดยไม่ใส่ \n
                text += line[1][0]
        return {"original_text": text.strip()}

    return {"original_text": "Unsupported file format"}