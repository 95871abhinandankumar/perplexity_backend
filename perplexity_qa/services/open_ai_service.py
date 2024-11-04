# services/openai_service.py
import os
import requests
from perplexity_backend import settings

def get_openai_response(user_message):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.LANGUAGE_MODEL_API_KEY}",  # Store your API key securely in environment variables
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": user_message}],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return {"status_code": response.status_code, "content": response.json()["choices"][0]["message"]["content"]}
    else:
        return {"status_code": response.status_code, "content":f"Error: {response.status_code}, {response.text}"}