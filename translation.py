from pulltext import text
import torch
import re
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL_NAME = "facebook/nllb-200-1.3B"

# เลือก device
device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME,
    dtype="auto",
    attn_implementation="sdpa"
).to(device)

# ตั้ง source language ให้ถูกต้อง
tokenizer.src_lang = "zho_Hans"

# 🔹 ทำความสะอาดข้อความก่อน
article = re.sub(r"\s+", " ", text).strip()


def translate_chunk(chunk):
    inputs = tokenizer(
        chunk,
        return_tensors="pt",
        truncation=True,
        max_length=512
    ).to(device)

    translated_tokens = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids("tha_Thai"),
        max_length=1000,
        num_beams=5,
        repetition_penalty=1.3,
        no_repeat_ngram_size=3,
        length_penalty=1.1,
        early_stopping=True
    )

    return tokenizer.batch_decode(
        translated_tokens,
        skip_special_tokens=True
    )[0]


# 🔹 ถ้าข้อความยาวมาก ให้แบ่ง chunk
def split_text(text, max_chars=1500):
    chunks = []
    for i in range(0, len(text), max_chars):
        chunks.append(text[i:i+max_chars])
    return chunks


chunks = split_text(article)
results = [translate_chunk(chunk) for chunk in chunks]

final_translation = "\n".join(results)

print(final_translation)
