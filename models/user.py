from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone = Column(String(20), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    profile_pic = Column(String(255))
    is_driver_active = Column(Boolean, default=False, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    driver_documents = relationship(
        "DriverDocument", back_populates="user", uselist=False)
    trips = relationship("Trip", back_populates="driver")
    bookings = relationship("Booking", back_populates="passenger")
    chats_sent = relationship(
        "Chat", back_populates="sender", foreign_keys='Chat.sender_id')
    chats_received = relationship(
        "Chat", back_populates="receiver", foreign_keys='Chat.receiver_id')
    reports_sent = relationship(
        "Report", foreign_keys="[Report.reporter_id]", back_populates="reporter")
    reports_received = relationship(
        "Report", foreign_keys="[Report.reported_user_id]", back_populates="reported_user")
    admin = relationship("Admin", back_populates="user", uselist=False)
    reviews_given = relationship(
        "Review", foreign_keys="[Review.reviewer_id]", back_populates="reviewer")
    reviews_received = relationship(
        "Review", foreign_keys="[Review.reviewee_id]", back_populates="reviewee")
