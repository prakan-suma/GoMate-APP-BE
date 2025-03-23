from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional
from decimal import Decimal

class TripStatus(str, Enum):
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

class BookingOut(BaseModel):
    id: int
    passenger_id: int
    passenger: UserOut
    status: str
    amount: int
    created_at: datetime

    class Config:
        from_attributes = True


class TripBase(BaseModel):
    origin: str
    destination: str
    latitude_des: Decimal
    longitude_des: Decimal
    departure_time: datetime
    available_seats: int
    fare: float
    status: Optional[TripStatus] = TripStatus.ongoing


class TripCreate(TripBase):
    driver_id: int


class TripUpdate(TripBase):
    pass

class TripOut(TripBase):
    id: int
    driver_id: int
    driver: UserOut
    bookings: Optional[list[BookingOut]] = None
    created_at: datetime

    class Config:
        from_attributes = True
