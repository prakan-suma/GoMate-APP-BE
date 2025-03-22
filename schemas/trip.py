from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional

class TripStatus(str, Enum):
    scheduled = "scheduled"
    ongoing = "ongoing"
    completed = "completed"
    canceled = "canceled"

class DriverDocumentOut(BaseModel):
    license_number: str
    vehicle_registration: str
    vehicle_brand: str
    vehicle_model: str
    vehicle_color: str
    
class UserOut(BaseModel):
    name: str
    email: str
    phone: str
    profile_pic: Optional[str]
    is_driver_active: bool
    driver_documents: Optional[DriverDocumentOut] 


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
    driver: UserOut 
    created_at: datetime

    class Config:
        from_attributes = True
        from_attributes = True
