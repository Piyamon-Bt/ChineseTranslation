from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from os import environ as env
from nodes.extract import extract_node  # นำเข้าฟังก์ชันที่คุณเขียนไว้
# from graph import build_graph
app = FastAPI()
# flow = build_graph()

# Allow frontend call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": f"FastAPI is secret = {env['MY_VARIABLE']} 🚀"}
# import os

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # อ่านไฟล์ทั้งหมดเข้า Memory (ตัวแปร content จะเป็น bytes)
    content = await file.read()

    # สร้าง Dictionary ตามโครงสร้างที่ extract_node ต้องการ
    state_input = {
        "file_bytes": content,
        "file_name": file.filename
    }

    # ส่งต่อให้ function ใน nodes.py
    try:
        result = extract_node(state_input)
    except Exception as e:
        return {"error": f"Internal processing error: {str(e)}"}

    return {
        "filename": file.filename,
        "extracted_text": result.get("original_text", "")
    }

# @app.post("/process-doc")
# async def process_document(file: UploadFile = File(...)):
#     # 1. อ่านไฟล์เป็น bytes
#     content = await file.read()
    
#     # 2. กำหนด Initial State (จุดเริ่มต้นของ Flow)
#     initial_input = {
#         "file_bytes": content,
#         "file_name": file.filename
#     }
    
#     # 3. รัน LangGraph (จะวิ่งผ่าน Extract -> Chunk -> Classify ... จนจบ)
#     final_state = await flow.ainvoke(initial_input)
    
#     # 4. ส่งผลลัพธ์กลับ
#     return {
#         "status": "success",
#         "original": final_state.get("original_text"),
#         "translation": final_state.get("translated_text")
#     }