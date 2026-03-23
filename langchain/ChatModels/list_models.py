import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    print("OPENROUTER_API_KEY not found in environment.")
    exit(1)

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

try:
    response = requests.get("https://openrouter.ai/api/v1/models", headers=headers)
    response.raise_for_status()
    models = response.json()["data"]
    
    print("Available Free Models:")
    for model in models:
        # Filter for free models or just print potentially compatible ones
        if "free" in model["id"].lower():
            print(f"- {model['id']}")
            
except Exception as e:
    print(f"Error fetching models: {e}")
