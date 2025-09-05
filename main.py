from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import engine, SessionLocal

# Import Base from models, not from database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/ride_request/", response_model=schemas.RideRequest)
def create_ride_request(ride_request: schemas.RideRequestCreate, db: Session = Depends(get_db)):
    return crud.create_ride_request(db=db, ride_request=ride_request)
