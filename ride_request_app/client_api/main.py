import requests
import json
import sys

API_URL = "http://127.0.0.1:8000/ride_request/"

def create_ride_request():
    print("\n=== Create New Ride Request ===")
    source = input("Enter pickup location: ")
    destination = input("Enter drop location: ")

    payload = {
        "user_id": 1,  # Using a default user_id for now
        "source": source,
        "destination": destination
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            print("\n✅ Ride request created successfully!")
            print("Request details:")
            print(json.dumps(response.json(), indent=4))
            
            # Verify the data was saved by showing the returned ID
            ride_id = response.json().get('id')
            print(f"\nRide request ID: {ride_id} (saved in database)")
        else:
            print(f"\n❌ Failed with status code: {response.status_code}")
            print("Error:", response.text)
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to the server")
        print("Make sure to start the FastAPI server first with:")
        print("uvicorn ride_request_app.server.main:app --reload")
        sys.exit(1)

def main():
    while True:
        print("\n=== Ride Request System ===")
        print("1. Create new ride request")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == "1":
            create_ride_request()
        elif choice == "2":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
