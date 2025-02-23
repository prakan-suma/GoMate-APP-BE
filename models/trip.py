from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, DECIMAL, TIMESTAMP
from sqlalchemy.orm import relationship
from database.session import Base
from sqlalchemy.sql import func
import enum

class TripStatusEnum(enum.Enum):
    scheduled = "scheduled"
    ongoing = "ongoing"
    completed = "completed"
    canceled = "canceled"

class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, autoincrement=True)
    driver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    origin = Column(String(255), nullable=False)
    destination = Column(String(255), nullable=False)
    departure_time = Column(DateTime, nullable=False)
    available_seats = Column(Integer, nullable=False)
    fare = Column(DECIMAL(10, 2), nullable=False)
    status = Column(Enum(TripStatusEnum), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    
    reports = relationship("Report", back_populates="trip") 
    driver = relationship("User", back_populates="trips")
    bookings = relationship("Booking", back_populates="trip")
    reviews = relationship("Review", back_populates="trip")