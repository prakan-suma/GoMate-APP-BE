from crud.booking import create_booking, get_all_bookings, get_booking, update_booking_status, cancel_booking
from schemas.booking import BookingCreate
from sqlalchemy.orm import Session

def create_booking_service(db: Session, booking: BookingCreate):
    return create_booking(db, booking)

def get_all_bookings_service(db: Session, user_id: int = None, skip: int = 0, limit: int = 10):
    return get_all_bookings(db, user_id, skip, limit)

def get_booking_service(db: Session, booking_id: int):
    return get_booking(db, booking_id)

def update_booking_status_service(db: Session, booking_id: int, status: str):
    # Fetch the booking
    db_booking = update_booking_status(db, booking_id, status)
    if not db_booking:
        return None

    # Return the updated booking in the correct format
    return {
        "id": db_booking.id,
        "trip_id": db_booking.trip_id,
        "passenger_id": db_booking.passenger_id,
        "status": db_booking.status,
        "booked_at": db_booking.booked_at,
        "message": "Booking status updated successfully"
    }

def cancel_booking_service(db: Session, booking_id: int):
    return cancel_booking(db, booking_id)