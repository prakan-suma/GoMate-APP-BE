from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from database.session import Base
import enum

class PaymentStatusEnum(enum.Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    status = Column(Enum(PaymentStatusEnum), nullable=False)
    paid_at = Column(TIMESTAMP)

    bookings = relationship("Booking", back_populates="payments")
