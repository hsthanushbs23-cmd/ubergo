from sqlalchemy.orm import Session
from . import models, schemas

# Driver operations
def create_driver(db: Session, driver: schemas.DriverCreate):
    db_driver = models.Driver(**driver.dict())
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver

def get_driver(db: Session, driver_id: int):
    return db.query(models.Driver).filter(models.Driver.id == driver_id).first()

def get_driver_rides(db: Session, driver_id: int):
    return db.query(models.RideRequest).filter(models.RideRequest.driver_id == driver_id).all()

def update_driver_status(db: Session, driver_id: int, status: str):
    db_driver = db.query(models.Driver).filter(models.Driver.id == driver_id).first()
    if db_driver:
        db_driver.status = status
        db.commit()
        db.refresh(db_driver)
    return db_driver

# Ride operations
def create_ride_request(db: Session, ride: schemas.RideRequestCreate):
    db_ride = models.RideRequest(
        source=ride.source,
        destination=ride.destination,
        status="pending"
    )
    db.add(db_ride)
    db.commit()
    db.refresh(db_ride)
    return db_ride

def get_rides_by_status(db: Session, status: str):
    return db.query(models.RideRequest).filter(models.RideRequest.status == status).all()

def get_ride(db: Session, ride_id: int):
    return db.query(models.RideRequest).filter(models.RideRequest.id == ride_id).first()

def accept_ride(db: Session, ride_id: int, driver_id: int):
    # Get the ride and driver
    db_ride = get_ride(db, ride_id)
    db_driver = get_driver(db, driver_id)
    
    if db_ride and db_driver and db_ride.status == "pending":
        # Update ride
        db_ride.status = "accepted"
        db_ride.driver_id = driver_id
        
        # Update driver status
        db_driver.status = "busy"
        
        db.commit()
        db.refresh(db_ride)
        db.refresh(db_driver)
        
    return db_ride

def complete_ride(db: Session, ride_id: int):
    db_ride = get_ride(db, ride_id)
    if db_ride and db_ride.status == "accepted":
        # Update ride status
        db_ride.status = "completed"
        
        # Update driver status back to available
        if db_ride.driver:
            db_ride.driver.status = "available"
        
        db.commit()
        db.refresh(db_ride)
        if db_ride.driver:
            db.refresh(db_ride.driver)
            
    return db_ride

