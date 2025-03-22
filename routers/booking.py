from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database.session import get_db
from crud.booking import (
    create_booking,
    get_booking,
    get_all_bookings,
    update_booking,
    delete_booking,
    get_bookings_by_user_id
)
from schemas.booking import BookingCreate, BookingUpdate, BookingResponse

router = APIRouter(prefix="/v1/booking", tags=["booking"])

@router.post("/", response_model=BookingResponse)
def create_booking_view(booking_data: BookingCreate, db: Session = Depends(get_db)):
    return create_booking(db, booking_data)


@router.get("/", response_model=List[BookingResponse])
def get_all_bookings_view(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    bookings = get_all_bookings(db, skip, limit)
    return bookings


@router.get("/{booking_id}", response_model=BookingResponse)
def get_booking_view(booking_id: int, db: Session = Depends(get_db)):
    booking = get_booking(db, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.get("/user/{user_id}", response_model=List[BookingResponse])
def get_bookings_by_user_id_view(
    user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    bookings = get_bookings_by_user_id(db, user_id, skip, limit)
    return bookings

@router.patch("/{booking_id}", response_model=dict)
def update_booking_view(
    booking_id: int, booking_data: BookingUpdate, db: Session = Depends(get_db)
):
    updated_booking = update_booking(db, booking_id, booking_data)
    if not updated_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return updated_booking


@router.delete("/{booking_id}")
def delete_booking_view(booking_id: int, db: Session = Depends(get_db)):
    if not delete_booking(db, booking_id):
        raise HTTPException(status_code=404, detail="Booking not found")
    return {'message': 'Booking deleted successfully'}
