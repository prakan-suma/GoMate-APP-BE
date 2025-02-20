from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class TripStatus(str, Enum):
    scheduled = "scheduled"
    ongoing = "ongoing"
    completed = "completed"
    canceled = "canceled"


class TripBase(BaseModel):
    origin: str
    destination: str
    departure_time: datetime
    available_seats: int
    fare: float
    status: TripStatus


class TripCreate(TripBase):
    driver_id: int


class TripUpdate(TripBase):
    status: TripStatus


class TripOut(TripBase):
    id: int
    driver_id: int
    created_at: datetime

    class Config:
        orm_mode = True
