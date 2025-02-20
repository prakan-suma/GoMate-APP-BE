from sqlalchemy import Column, Integer, ForeignKey, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from database.session import Base
from sqlalchemy.sql import func


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, autoincrement=True)
    reporter_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    reported_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    trip_id = Column(Integer, ForeignKey("trips.id"), nullable=True)
    issue = Column(Text, nullable=False)
    reported_at = Column(TIMESTAMP, server_default=func.now())

    reporter = relationship("User", foreign_keys=[reporter_id], back_populates="reports_sent")
    reported_user = relationship("User", foreign_keys=[reported_user_id], back_populates="reports_received")
    trip = relationship("Trip", back_populates="reports")