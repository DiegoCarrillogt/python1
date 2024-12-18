import requests
import json

response = requests.get("https://api.openai.com/v1/chat/completions")
print(response.json())

if response.status_code == 200:
    print("Request successful")
else:
    print(f"Request failed with status code {response.status_code}")

