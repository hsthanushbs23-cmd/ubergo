from pydantic import BaseModel

class RideRequestBase(BaseModel):
    user_id: int
    source: str
    destination: str

class RideRequestCreate(RideRequestBase):
    pass

class RideRequest(RideRequestBase):
    id: int

    class Config:
        orm_mode = True
