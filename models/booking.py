from sqlalchemy import Column, Integer, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from database.session import Base
from sqlalchemy.sql import func
import enum

class BookingStatusEnum(enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    canceled = "canceled"

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    trip_id = Column(Integer, ForeignKey("trips.id"), nullable=False)
    passenger_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(Enum(BookingStatusEnum), nullable=False)
    booked_at = Column(TIMESTAMP, server_default=func.now())
    payments = relationship("Payment", back_populates="booking")
    trip = relationship("Trip", back_populates="bookings")
    passenger = relationship("User", back_populates="bookings")
