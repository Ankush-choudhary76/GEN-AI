import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

print(f"Key: {api_key[:5]}...")

url = "https://openrouter.ai/api/v1/embeddings"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost:3000", # Optional
}
data = {
    "model": "openai/text-embedding-3-small",
    "input": "test"
}

response = requests.post(url, headers=headers, json=data)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
