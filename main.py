import requests
import json

API_URL = "http://127.0.0.1:8000/ride_request/"


payload = {
    "user_id": 1,
    "source": "Bangalore",
    "destination": "Mysore"
}


response = requests.post(API_URL, json=payload)

if response.status_code == 200:
    print("✅ Ride request created successfully!")
    print("Response:", json.dumps(response.json(), indent=4))
else:
    print(" Failed with status code:", response.status_code)
    print("Response:", response.text)
