from typing import Optional
from pydantic import BaseModel

class DriverBase(BaseModel):
    name: str
    status: str = "available"

class DriverCreate(DriverBase):
    pass

class Driver(DriverBase):
    id: int

    class Config:
        from_attributes = True

class RideRequestBase(BaseModel):
    source: str
    destination: str

class RideRequestCreate(RideRequestBase):
    pass

class RideRequest(RideRequestBase):
    id: int
    status: str = "pending"
    driver_id: Optional[int] = None

    class Config:
        from_attributes = True

class AcceptRide(BaseModel):
    driver_id: int
