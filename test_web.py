#!/usr/bin/env python3

import requests
import time

def test_web_pages():
    base_url = "http://localhost:8000"
    
    print("🌐 Testing Web Pages...")
    print("=" * 50)
    
    # Test main page
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✅ Main page (/) - Working")
        else:
            print(f"❌ Main page (/) - Error {response.status_code}")
    except Exception as e:
        print(f"❌ Main page (/) - Connection error: {e}")
    
    # Test driver page
    try:
        response = requests.get(f"{base_url}/driver?driver_id=1")
        if response.status_code == 200:
            print("✅ Driver page (/driver?driver_id=1) - Working")
        else:
            print(f"❌ Driver page - Error {response.status_code}")
    except Exception as e:
        print(f"❌ Driver page - Connection error: {e}")
    
    # Test API endpoints
    try:
        response = requests.get(f"{base_url}/rides/?status=pending")
        if response.status_code == 200:
            rides = response.json()
            print(f"✅ API (/rides) - Working, {len(rides)} pending rides")
        else:
            print(f"❌ API (/rides) - Error {response.status_code}")
    except Exception as e:
        print(f"❌ API (/rides) - Connection error: {e}")
    
    print("\n🚀 Server URLs:")
    print(f"   Main page: {base_url}/")
    print(f"   Basha (Driver 1): {base_url}/driver?driver_id=1")
    print(f"   Rocky Bhai (Driver 2): {base_url}/driver?driver_id=2")
    print(f"   Dboss (Driver 3): {base_url}/driver?driver_id=3")

if __name__ == "__main__":
    print("Waiting 2 seconds for server to fully start...")
    time.sleep(2)
    test_web_pages()