from sqlalchemy import Column, Integer, String
from .database import Base

class RideRequest(Base):
    __tablename__ = "ride_requests"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    source = Column(String, nullable=False)
    destination = Column(String, nullable=False)
