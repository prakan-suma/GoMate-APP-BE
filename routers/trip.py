from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.trip import TripCreate, TripUpdate, TripOut
from services.trip import create_trip_service, update_trip_service
from database.session import get_db

router = APIRouter(prefix="/v1/trips", tags=["trips"])

@router.post("/", response_model=TripOut)
def create_trip_view(trip: TripCreate, db: Session = Depends(get_db)):
    return create_trip_service(db=db, trip=trip)

@router.put("/{trip_id}", response_model=TripOut)
def update_trip_view(trip_id: int, trip: TripUpdate, db: Session = Depends(get_db)):
    return update_trip_service(db=db, trip_id=trip_id, trip=trip)
