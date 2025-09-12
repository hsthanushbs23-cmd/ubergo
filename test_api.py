#!/usr/bin/env python3

import requests

def test_driver_api():
    try:
        # Test get driver endpoint
        print("Testing driver API endpoints...")
        
        # Test driver 1
        response = requests.get("http://localhost:8000/get_driver/1")
        if response.status_code == 200:
            driver = response.json()
            print(f"✅ Driver 1: {driver}")
        else:
            print(f"❌ Driver 1 API failed: {response.status_code}")
            
        # Test rides endpoint
        response = requests.get("http://localhost:8000/rides/?status=pending")
        if response.status_code == 200:
            rides = response.json()
            print(f"✅ Pending rides: {len(rides)} rides")
        else:
            print(f"❌ Rides API failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error connecting to server: {e}")
        print("Make sure server is running on http://localhost:8000")

if __name__ == "__main__":
    test_driver_api()