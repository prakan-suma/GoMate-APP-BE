from pydantic import BaseModel
from datetime import datetime

class BookingCreate(BaseModel):
    trip_id: int
    passenger_id: int

class BookingOut(BaseModel):
    id: int  # Changed from booking_id to id
    trip_id: int
    passenger_id: int
    status: str
    booked_at: datetime
    message: str = "Booking created successfully"

class UpdateBookingStatus(BaseModel):
    status: str  # Define the status field in the request body