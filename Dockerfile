# # ใช้ python version ที่คุณมี
# FROM python:3.10-slim

# WORKDIR /app

# COPY . /app

# # copy requirements ก่อน (optimize cache)
# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# # run server
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]



# 1. ใช้ Python 3.10-slim เหมือนเดิม
FROM python:3.10-slim

# 2. ติดตั้ง System Dependencies (สำคัญมาก: ถ้าไม่ลง PaddleOCR จะ Error หา lib ไม่เจอ)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libgomp1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 3. Copy requirements.txt มาลงก่อน เพื่อให้ Docker ไม่ต้องลง Library ใหม่ทุกครั้งที่แก้ Code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. (Optional) สั่งโหลด Model ภาษาจีนเตรียมไว้ใน Image เลย 
# บรรทัดนี้จะทำให้ Build นานขึ้นนิดหน่อย แต่เวลา 'docker up' แล้ว API จะพร้อมใช้งานทันที
RUN python3 -c "from paddleocr import PaddleOCR; PaddleOCR(use_angle_cls=True, lang='ch')"

# 5. Copy ไฟล์ทั้งหมดในโปรเจกต์ (รวมถึง main.py, nodes.py) เข้าไปใน Docker
COPY . .

# 6. แก้ไข CMD: 
# ถ้าโครงสร้างคุณคือ /app/main.py ให้ใช้ "main:app" 
# แต่ถ้าไฟล์อยู่ใน folder app/ ให้ใช้ "app.main:app" ตามเดิมครับ
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]