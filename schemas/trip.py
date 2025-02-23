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
    document_status: str
    
class UserOut(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    profile_pic: Optional[str]
    is_driver_active: bool
    created_at: datetime
    driver_documents: Optional[list[DriverDocumentOut]] 


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
        orm_mode = True
        from_attributes = True
