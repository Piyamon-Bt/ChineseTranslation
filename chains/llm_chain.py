# from langchain_community.llms import HuggingFaceHub
# import os

# def get_llm():
#     return HuggingFaceHub(
#         repo_id="Qwen/Qwen2.5-7B-Instruct",
#         huggingfacehub_api_token=os.getenv("HF_API_KEY"),
#         model_kwargs={"temperature": 0.2, "max_new_tokens": 512}
#     )

from google import genai

client = genai.Client(api_key="ใส่_API_KEY_ของคุณที่นี่")
response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents="ช่วยแปลประโยคนี้เป็นภาษาจีน: วันนี้อากาศดีมาก"
)
print(response.text)