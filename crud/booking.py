from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Booking,Trip
from schemas.booking import BookingCreate, BookingUpdate


def create_booking(db: Session, booking_data: BookingCreate) -> Booking:
    booking = Booking(**booking_data.dict(), status="pending")
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking


def get_booking(db: Session, booking_id: int) -> Booking:
    return db.query(Booking).filter(Booking.id == booking_id).first()


def get_all_bookings(db: Session, skip: int = 0, limit: int = 10) -> list:
    return db.query(Booking).offset(skip).limit(limit).all()


def get_bookings_by_user_id(db: Session, user_id: int, skip: int = 0, limit: int = 10) -> list:
    return db.query(Booking).filter(Booking.passenger_id == user_id).offset(skip).limit(limit).all()


def update_booking(
    db: Session, booking_id: int, booking_data: BookingUpdate
) -> Booking:
    
    booking = get_booking(db, booking_id)
    trip = db.query(Trip).filter(Trip.id == booking.trip_id).first()
    
    if not booking:
        raise HTTPException(
            status_code=404, detail="Driver document not found")

    for var, value in booking_data.dict(exclude_unset=True).items():
        setattr(booking, var, value)
    db.commit()
    db.refresh(booking)
    
    trip.available_seats -= booking.amount
    db.commit()
    db.refresh(trip)

    return {"booking_id": booking.id, "message": "Booking status updated successfully"}


def delete_booking(db: Session, booking_id: int) -> bool:
    booking = get_booking(db, booking_id)
    if booking:
        db.delete(booking)
        db.commit()
        return True
    return False
