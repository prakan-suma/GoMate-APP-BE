from sqlalchemy.orm import Session
from models import Booking
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


def update_booking(
    db: Session, booking_id: int, booking_data: BookingUpdate
) -> Booking:
    booking = get_booking(db, booking_id)
    if booking:
        for var, value in booking_data.dict(exclude_unset=True).items():
            setattr(booking, var, value)
        db.commit()
    return booking


def delete_booking(db: Session, booking_id: int) -> bool:
    booking = get_booking(db, booking_id)
    if booking:
        db.delete(booking)
        db.commit()
        return True
    return False
