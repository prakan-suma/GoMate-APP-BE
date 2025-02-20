from sqlalchemy import Column, Integer, ForeignKey, String, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from database.session import Base
from sqlalchemy.sql import func

class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    receiver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    message = Column(Text, nullable=False)
    sent_at = Column(TIMESTAMP, server_default=func.now())

    sender = relationship("User", back_populates="chats_sent", foreign_keys=[sender_id])
    receiver = relationship("User", back_populates="chats_received", foreign_keys=[receiver_id])
