#!/usr/bin/env python3

# Direct database query to verify driver names
from ride_request_app.server.database import SessionLocal, engine
from ride_request_app.server import models
from sqlalchemy import text

def check_database_directly():
    db = SessionLocal()
    try:
        print("🔍 Direct PostgreSQL Database Check:")
        print("=" * 50)
        
        # Check drivers table structure and content
        print("📋 DRIVERS TABLE:")
        drivers = db.execute(text("SELECT * FROM drivers")).fetchall()
        print("Columns: id | name | status")
        print("-" * 30)
        for driver in drivers:
            print(f"{driver[0]} | {driver[1]} | {driver[2]}")
        
        print("\n📋 RIDE_REQUESTS TABLE:")
        rides = db.execute(text("SELECT * FROM ride_requests")).fetchall()
        print("Columns: id | source | destination | status | driver_id")
        print("-" * 60)
        for ride in rides:
            print(f"{ride[0]} | {ride[1]} | {ride[2]} | {ride[3]} | {ride[4]}")
            
        print("\n🔗 RIDES WITH DRIVER NAMES (JOIN):")
        join_query = text("""
            SELECT r.id, r.source, r.destination, r.status, d.name 
            FROM ride_requests r 
            LEFT JOIN drivers d ON r.driver_id = d.id
        """)
        joined_data = db.execute(join_query).fetchall()
        print("ride_id | source | destination | status | driver_name")
        print("-" * 70)
        for row in joined_data:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4] or 'No Driver'}")
            
    except Exception as e:
        print(f"❌ Database error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    check_database_directly()