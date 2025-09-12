from ride_request_app.server.database import engine
import sys

def test_connection():
    try:
        # Try to connect and execute a simple query
        with engine.connect() as connection:
            from sqlalchemy import text
            result = connection.execute(text("SELECT 1"))
            print("✅ Successfully connected to PostgreSQL!")
            return True
    except Exception as e:
        print("❌ Database connection failed!")
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_connection()
    if not success:
        sys.exit(1)
