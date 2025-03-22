from pydantic import BaseModel
from datetime import datetime

class PriceGuidelineOut(BaseModel):
    id: int
    base_price: float
    price_per_km: float
    created_at: datetime

    class Config:
        from_attributes = True  # Enable ORM mode