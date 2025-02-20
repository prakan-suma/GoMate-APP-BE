from sqlalchemy import Column, Integer, ForeignKey, String, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from database.session import Base
from sqlalchemy.sql import func


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    trip_id = Column(Integer, ForeignKey("trips.id"), nullable=False)
    reviewer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    reviewee_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text)
    reviewed_at = Column(TIMESTAMP, server_default=func.now())

    trip = relationship("Trip", back_populates="reviews")
    reviewer = relationship("User", foreign_keys=[
                            reviewer_id], back_populates="reviews_given")
    reviewee = relationship("User", foreign_keys=[
                            reviewee_id], back_populates="reviews_received")
