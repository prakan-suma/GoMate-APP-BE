from sqlalchemy import Column, Integer, String, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from database.session import Base
from sqlalchemy.sql import func
import enum

class DocumentStatusEnum(enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

class DriverDocument(Base):
    __tablename__ = "driver_documents"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    license_number = Column(String(50), nullable=False)
    vehicle_registration = Column(String(50), nullable=False)
    vehicle_brand = Column(String(50), nullable=False)
    vehicle_model = Column(String(50), nullable=False)
    vehicle_color = Column(String(20), nullable=False)
    document_status = Column(Enum(DocumentStatusEnum), default=DocumentStatusEnum.pending, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    user = relationship("User", back_populates="driver_documents")
