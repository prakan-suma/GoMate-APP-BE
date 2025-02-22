from sqlalchemy.orm import Session
from models.booking import Booking
from models.trip import Trip
from models.user import User
from fastapi import HTTPException
from schemas.booking import BookingCreate

def create_booking(db: Session, booking: BookingCreate):
    # Check if the trip exists
    trip = db.query(Trip).filter(Trip.id == booking.trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    # Check if the passenger exists
    passenger = db.query(User).filter(User.id == booking.passenger_id).first()
    if not passenger:
        raise HTTPException(status_code=404, detail="Passenger not found")

    # Create the booking
    db_booking = Booking(**booking.dict(), status="pending")
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)

    # Return the response in the correct format
    return {
        "id": db_booking.id,  # Use id instead of booking_id
        "trip_id": db_booking.trip_id,
        "passenger_id": db_booking.passenger_id,
        "status": db_booking.status,
        "booked_at": db_booking.booked_at,
        "message": "Booking created successfully"
    }

def get_booking(db: Session, booking_id: int):
    return db.query(Booking).filter(Booking.id == booking_id).first()

def get_all_bookings(db: Session, user_id: int = None, skip: int = 0, limit: int = 10):
    query = db.query(Booking)
    if user_id:
        query = query.filter((Booking.passenger_id == user_id) | (Booking.trip.has(driver_id=user_id)))
    return query.offset(skip).limit(limit).all()

def update_booking_status(db: Session, booking_id: int, status: str):
    # Fetch the booking
    db_booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not db_booking:
        return None

    # Update the status
    db_booking.status = status
    db.commit()
    db.refresh(db_booking)

    # Return the updated booking
    return db_booking

def cancel_booking(db: Session, booking_id: int):
    db_booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not db_booking:
        return None
    db.delete(db_booking)
    db.commit()
    return db_booking