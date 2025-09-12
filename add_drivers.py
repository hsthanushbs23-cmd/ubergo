#!/usr/bin/env python3

# Script to add sample drivers for testing
from ride_request_app.server.database import SessionLocal
from ride_request_app.server import models

def add_sample_drivers():
    db = SessionLocal()
    try:
        # Update existing drivers with new names
        drivers_data = [
            {"id": 1, "name": "Basha"},
            {"id": 2, "name": "Rocky Bhai"},
            {"id": 3, "name": "Dboss"}
        ]
        
        for driver_data in drivers_data:
            driver = db.query(models.Driver).filter(models.Driver.id == driver_data["id"]).first()
            if driver:
                driver.name = driver_data["name"]
                driver.status = "available"
            else:
                # Create new driver if doesn't exist
                new_driver = models.Driver(name=driver_data["name"], status="available")
                db.add(new_driver)
        
        db.commit()
        print("✅ Movie star drivers updated:")
        
        # Display updated drivers
        all_drivers = db.query(models.Driver).all()
        for driver in all_drivers:
            print(f"  - Driver {driver.id}: {driver.name} ({driver.status})")
            
    finally:
        db.close()

if __name__ == "__main__":
    add_sample_drivers()