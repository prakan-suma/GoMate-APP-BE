from pydantic import BaseModel
from datetime import datetime

class BookingCreate(BaseModel):
    trip_id: int
    passenger_id: int

class BookingOut(BaseModel):
    booking_id: int  # Changed from id to booking_id
    message: str = "Booking created successfully"

class UpdateBookingStatus(BaseModel):
    status: str  # Define the status field in the request body

class StatusUpdateResponse(BaseModel):
    message: str

class BookingDetail(BaseModel):
    booking_id: int
    trip_id: int
    passenger_id: int
    status: str
    booked_at: datetime

class BookingsResponse(BaseModel):
    bookings: list[BookingDetail]