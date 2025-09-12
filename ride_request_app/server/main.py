from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import os
from typing import List

from . import models, schemas, crud
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Setup templates with absolute path
template_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "templates")
print(f"Template directory: {template_dir}")
templates = Jinja2Templates(directory=template_dir)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User routes
@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    try:
        rides = db.query(models.RideRequest).order_by(models.RideRequest.id.desc()).limit(5).all()
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "rides": rides,
                "success_message": None,
                "error_message": None
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "rides": [],
                "success_message": None,
                "error_message": str(e)
            }
        )

@app.post("/ride_request/", response_model=schemas.RideRequest)
def create_ride_request(ride_request: schemas.RideRequestCreate, db: Session = Depends(get_db)):
    return crud.create_ride_request(db=db, ride=ride_request)

# Driver routes
@app.get("/driver")
def driver_page(request: Request, driver_id: int = None):
    return templates.TemplateResponse(
        "driver.html",
        {
            "request": request,
            "driver_id": driver_id
        }
    )

@app.get("/rides/", response_model=List[schemas.RideRequest])
def get_rides(status: str = "pending", db: Session = Depends(get_db)):
    rides = crud.get_rides_by_status(db, status)
    return rides

@app.get("/get_driver/{driver_id}", response_model=schemas.Driver)
def get_driver_details(driver_id: int, db: Session = Depends(get_db)):
    driver = crud.get_driver(db, driver_id)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver

@app.get("/my_rides/{driver_id}", response_model=List[schemas.RideRequest])
def get_driver_rides(driver_id: int, db: Session = Depends(get_db)):
    driver = crud.get_driver(db, driver_id)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return crud.get_driver_rides(db, driver_id)

@app.post("/accept_ride/{ride_id}")
def accept_ride(ride_id: int, accept_data: schemas.AcceptRide, db: Session = Depends(get_db)):
    ride = crud.accept_ride(db, ride_id, accept_data.driver_id)
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found or already accepted")
    return ride

@app.post("/complete_ride/{ride_id}", response_model=schemas.RideRequest)
def complete_ride(ride_id: int, db: Session = Depends(get_db)):
    ride = crud.complete_ride(db, ride_id)
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found or not in accepted state")
    return ride
