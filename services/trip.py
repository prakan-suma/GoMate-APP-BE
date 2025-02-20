from crud.trip import create_trip, update_trip
from schemas.trip import TripCreate, TripUpdate
from sqlalchemy.orm import Session

def create_trip_service(db: Session, trip: TripCreate):
    return create_trip(db, trip)

def update_trip_service(db: Session, trip_id: int, trip: TripUpdate):
    return update_trip(db, trip_id, trip)
