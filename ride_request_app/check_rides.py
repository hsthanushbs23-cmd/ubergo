from ride_request_app.server.database import engine
from sqlalchemy import text

def check_ride_requests():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM ride_requests ORDER BY id DESC"))
            rows = result.fetchall()
            
            if not rows:
                print("\n❌ No ride requests found in database")
                return
            
            print("\n=== Latest Ride Requests ===")
            for row in rows:
                print(f"\nRide ID: {row.id}")
                print(f"User ID: {row.user_id}")
                print(f"From: {row.source}")
                print(f"To: {row.destination}")
                print("-" * 30)
                
    except Exception as e:
        print("\n❌ Error accessing database:")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    check_ride_requests()
