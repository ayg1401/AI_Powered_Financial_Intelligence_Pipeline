import requests
import json

API_KEY = ""

url = f"https://newsapi.org/v2/everything?q=stock market&apiKey={API_KEY}"

response = requests.get(url)

print("STATUS CODE:", response.status_code)

data = response.json()

print(json.dumps(data, indent=2))