from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from schemas.trip import TripCreate, TripUpdate, TripOut
from services.trip import create_trip_service, get_trips_all_service, update_trip_service, get_trip_detail_service, delete_trip_service, get_trips_by_user_ids_service
from database.session import get_db
from typing import List

router = APIRouter(prefix="/v1/trips", tags=["trips"])


@router.get("/all", response_model=List[TripOut])
def get_all_trips_view(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_trips_all_service(db, skip, limit)


@router.get("/", response_model=List[TripOut])
def get_trips_from_user_id_view(user_ids: List[int] = Query(..., description="List of user IDs"),
                                skip: int = 0,
                                limit: int = 10,
                                db: Session = Depends(get_db)
                                ):
    return get_trips_by_user_ids_service(db, user_ids, skip, limit)


@router.get("/{trip_id}", response_model=TripOut)
def get_trip_detail_view(trip_id: int, db: Session = Depends(get_db)):
    trip = get_trip_detail_service(db=db, trip_id=trip_id)
    if not trip:
        return HTTPException(status_code=404, detail="Trip not found or someting wrong.")
    return trip


@router.post("/", response_model=TripOut)
def create_trip_view(trip: TripCreate, db: Session = Depends(get_db)):
    return create_trip_service(db=db, trip=trip)


@router.put("/{trip_id}", response_model=dict)
def update_trip_view(trip_id: int, trip: TripUpdate, db: Session = Depends(get_db)):
    return update_trip_service(db=db, trip_id=trip_id, trip=trip)


@router.delete("/{trip_id}")
def delete_trip_view(trip_id: int, db: Session = Depends(get_db)):
    if delete_trip_service(db, trip_id):
        return {"message": "Trip deleted successfully"}
    return {"message": "Trip not found"}
