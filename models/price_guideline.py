from sqlalchemy import Column, Integer, DECIMAL, TIMESTAMP
from database.session import Base
from sqlalchemy.sql import func

class PriceGuideline(Base):
    __tablename__ = "price_guidelines"

    id = Column(Integer, primary_key=True, autoincrement=True)
    base_price = Column(DECIMAL(10, 2), nullable=False)
    price_per_km = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
