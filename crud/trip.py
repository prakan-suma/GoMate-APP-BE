from sqlalchemy.orm import Session
from models.trip import Trip
from schemas.trip import TripCreate, TripUpdate

def create_trip(db: Session, trip: TripCreate):
    db_trip = Trip(**trip.dict())
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip

def update_trip(db: Session, trip_id: int, trip: TripUpdate):
    db_trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if db_trip:
        for key, value in trip.dict(exclude_unset=True).items():
            setattr(db_trip, key, value)
        db.commit()
        db.refresh(db_trip)
    return db_trip

def get_trip(db: Session, trip_id: int):
    return db.query(Trip).filter(Trip.id == trip_id).first()

def get_trips(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Trip).offset(skip).limit(limit).all()
