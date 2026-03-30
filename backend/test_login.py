import requests
import json

url = "https://sized-carita-flowerless.ngrok-free.dev/api/login/"
payload = {
    "username": "admin@safepulse.com",
    "password": "admin12"
}
headers = {
    "Content-Type": "application/json",
    "ngrok-skip-browser-warning": "true"
}

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
