from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BookingBase(BaseModel):
    trip_id: int
    passenger_id: int
    amount: int


class BookingCreate(BaseModel):
    trip_id: int
    passenger_id: int
    amount: int


class BookingUpdate(BaseModel):
    status: Optional[str]


class BookingResponse(BookingBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
