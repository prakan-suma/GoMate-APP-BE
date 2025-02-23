from crud.trip import create_trip, update_trip, get_trip_details, get_trips_by_user_ids, delete_trip,get_trips_all
from schemas.trip import TripCreate, TripUpdate
from sqlalchemy.orm import Session


def create_trip_service(db: Session, trip: TripCreate):
    return create_trip(db, trip)


def update_trip_service(db: Session, trip_id: int, trip: TripUpdate):
    return update_trip(db, trip_id, trip)


def get_trip_detail_service(db: Session, trip_id: int):
    return get_trip_details(db, trip_id)

def get_trips_by_user_ids_service(db: Session, user_ids: list[int], skip: int = 0, limit: int = 10):
    trips = get_trips_by_user_ids(db, user_ids, skip, limit)
    return trips

def get_trips_all_service(db: Session, skip: int = 0, limit: int = 10):
    trips = get_trips_all(db, skip, limit)
    return trips

def delete_trip_service(db: Session, trip_id: int):
    return delete_trip(db, trip_id)

