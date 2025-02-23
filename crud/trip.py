from sqlalchemy.orm import Session, joinedload
from models.trip import Trip
from models.user import User
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


def get_trips_by_user_ids(db: Session, user_ids: list[int], skip: int = 0, limit: int = 10):
    trips = (
        db.query(Trip)
        .options(joinedload(Trip.driver).joinedload(User.driver_documents))
        .filter(Trip.driver_id.in_(user_ids))
        .offset(skip)
        .limit(limit)
        .all()
    )

    return trips


def get_trip_details(db: Session, trip_id: int):
    trip = db.query(Trip).options(
        joinedload(Trip.driver).joinedload(User.driver_documents)
    ).filter(Trip.id == trip_id).first()

    if not trip:
        return None

    return trip


def get_trips_all(db: Session, skip: int = 0, limit: int = 10):
    trips = (
        db.query(Trip)
        .options(joinedload(Trip.driver).joinedload(User.driver_documents))
        .offset(skip)
        .limit(limit)
        .all()
    )
    return trips


def delete_trip(db: Session, trip_id: int):
    db_trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if db_trip:
        db.delete(db_trip)
        db.commit()
        return True
    return False
