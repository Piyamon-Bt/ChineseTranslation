import requests
import os

HF_API_KEY = os.getenv("HF_API_KEY")
MODEL_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-7B-Instruct"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def query_llm(prompt: str):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 512}
    }

    response = requests.post(MODEL_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(response.text)

    return response.json()[0]["generated_text"]
