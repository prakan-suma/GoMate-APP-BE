from crud.booking import create_booking, get_all_bookings, get_booking, update_booking_status, cancel_booking
from schemas.booking import BookingCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException

def create_booking_service(db: Session, booking: BookingCreate):
    return create_booking(db, booking)

def get_all_bookings_service(db: Session, user_id: int = None, skip: int = 0, limit: int = 10):
    return get_all_bookings(db, user_id, skip, limit)

def get_booking_service(db: Session, booking_id: int):
    booking = get_booking(db, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

def update_booking_status_service(db: Session, booking_id: int, status: str):
    # Call the CRUD function to update the status
    result = update_booking_status(db, booking_id, status)
    if not result:
        raise HTTPException(status_code=404, detail="Booking not found")
    return result

def cancel_booking_service(db: Session, booking_id: int):
    return cancel_booking(db, booking_id)