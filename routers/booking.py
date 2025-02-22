from fastapi import APIRouter, Depends, HTTPException
from database.session import get_db
from sqlalchemy.orm import Session
from schemas.booking import BookingCreate, BookingOut, UpdateBookingStatus, BookingsResponse, BookingDetail, StatusUpdateResponse
from services.booking import (
    create_booking_service,
    get_all_bookings_service,
    get_booking_service,
    update_booking_status_service,
    cancel_booking_service
)

router = APIRouter(prefix="/v1/bookings", tags=["bookings"])

@router.post("/", response_model=BookingOut)
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    return create_booking_service(db=db, booking=booking)

@router.get("/", response_model=BookingsResponse)
def get_all_bookings(
    user_id: int = None, 
    skip: int = 0, 
    limit: int = 10, 
    db: Session = Depends(get_db)
):
    return get_all_bookings_service(db, user_id, skip, limit)

@router.get("/{booking_id}", response_model=BookingDetail)
def get_booking_details(booking_id: int, db: Session = Depends(get_db)):
    booking = get_booking_service(db, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.patch("/{booking_id}/status", response_model=StatusUpdateResponse)
def update_booking_status(
    booking_id: int, 
    update_data: UpdateBookingStatus,  # Use the schema for the request body
    db: Session = Depends(get_db)
):
    # Call the service to update the booking status
    result = update_booking_status_service(db, booking_id, update_data.status)
    if not result:
        raise HTTPException(status_code=404, detail="Booking not found")
    return result

@router.delete("/{booking_id}", response_model=dict)
def cancel_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = cancel_booking_service(db, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"message": "Booking canceled successfully"}