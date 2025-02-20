from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database.session import Base
import enum

class RoleEnum(enum.Enum):
    superadmin = "superadmin"
    moderator = "moderator"

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    role = Column(Enum(RoleEnum), nullable=False)

    user = relationship("User", back_populates="admin")
