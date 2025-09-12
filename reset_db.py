from ride_request_app.server.database import engine
from sqlalchemy import text
from ride_request_app.server.models import Base

def reset_database():
    # Drop existing tables
    with engine.connect() as conn:
        conn.execute(text('DROP TABLE IF EXISTS ride_requests CASCADE'))
        conn.execute(text('DROP TABLE IF EXISTS drivers CASCADE'))
        conn.commit()
    
    # Create new tables
    Base.metadata.create_all(bind=engine)
    
    # Create a test driver
    with engine.connect() as conn:
        conn.execute(text("INSERT INTO drivers (name, status) VALUES ('Test Driver', 'available')"))
        conn.commit()

if __name__ == "__main__":
    reset_database()
    print("Database reset complete!")
