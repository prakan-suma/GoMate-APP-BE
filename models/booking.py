from sqlalchemy import Column, Integer, ForeignKey, String, Enum as SQLEnum, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.session import Base
import enum


class BookingStatus(enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    trip_id = Column(Integer, ForeignKey("trips.id"), nullable=False)
    passenger_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(
        SQLEnum(BookingStatus), default=BookingStatus.pending, nullable=False
    )
    created_at = Column(TIMESTAMP, server_default=func.now())

    payments = relationship("Payment", back_populates="bookings")
    trip = relationship("Trip", back_populates="bookings")
    passenger = relationship("User", back_populates="bookings")
