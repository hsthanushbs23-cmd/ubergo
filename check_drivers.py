#!/usr/bin/env python3

# Script to check drivers in database
from ride_request_app.server.database import SessionLocal
from ride_request_app.server import models

def check_drivers():
    db = SessionLocal()
    try:
        drivers = db.query(models.Driver).all()
        print("🏏 Current Cricket Star Drivers:")
        print("=" * 40)
        for driver in drivers:
            print(f"Driver {driver.id}: {driver.name} ({driver.status})")
        print("=" * 40)
        
        # Also check rides
        rides = db.query(models.RideRequest).all()
        print(f"\n📱 Total Rides in System: {len(rides)}")
        for ride in rides:
            driver_name = ride.driver.name if ride.driver else "No Driver"
            print(f"  Ride #{ride.id}: {ride.source} → {ride.destination} | Status: {ride.status} | Driver: {driver_name}")
            
    finally:
        db.close()

if __name__ == "__main__":
    check_drivers()