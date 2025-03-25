# routers/live_tracking.py
from fastapi import APIRouter, Depends, HTTPException
from redis.asyncio import Redis
from typing import Dict, List
import json
from geopy.distance import geodesic
from database.redis import get_redis  # Import get_redis from database/redis.py

router = APIRouter(prefix="/v1/live-tracking", tags=["live-tracking"])

# Dependency injection for Redis
async def get_redis_client(redis: Redis = Depends(get_redis)) -> Redis:
    return redis

@router.post("/driver/{driver_id}")
async def update_driver_location_view(driver_id: int, location: Dict, redis: Redis = Depends(get_redis_client)):
    try:
        key = f"driver:{driver_id}:location"
        await redis.set(key, json.dumps(location))
        return {"message": "Driver's location updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update driver location: {str(e)}")

@router.post("/passenger/{passenger_id}")
async def update_passenger_location_view(passenger_id: int, location: Dict, redis: Redis = Depends(get_redis_client)):
    try:
        key = f"passenger:{passenger_id}:location"
        await redis.set(key, json.dumps(location))
        return {"message": "Passenger's location updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update passenger location: {str(e)}")

@router.get("/drivers")
async def get_all_drivers(redis: Redis = Depends(get_redis_client)):
    try:
        driver_keys = await redis.keys("driver:*:location")
        drivers = []

        for driver_key in driver_keys:
            driver_location = await redis.get(driver_key)
            if driver_location:
                driver_location = json.loads(driver_location)
                driver_id = driver_key.split(":")[1]
                drivers.append({"driver_id": driver_id, "location": driver_location})

        return {"drivers": drivers}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch drivers: {str(e)}")

@router.get("/passengers")
async def get_all_passengers(redis: Redis = Depends(get_redis_client)):
    try:
        passenger_keys = await redis.keys("passenger:*:location")
        passengers = []

        for passenger_key in passenger_keys:
            passenger_location = await redis.get(passenger_key)
            if passenger_location:
                passenger_location = json.loads(passenger_location)
                passenger_id = passenger_key.split(":")[1]
                passengers.append({"passenger_id": passenger_id, "location": passenger_location})

        return {"passengers": passengers}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch passengers: {str(e)}")

@router.get("/driver/{driver_id}")
async def get_driver_location(driver_id: int, redis: Redis = Depends(get_redis_client)):
    try:
        key = f"driver:{driver_id}:location"
        driver_location = await redis.get(key)
        if not driver_location:
            return {"message": "Driver's location not found"}
        return {"driver_id": driver_id, "location": json.loads(driver_location)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch driver location: {str(e)}")

@router.get("/passenger/{passenger_id}")
async def get_passenger_location(passenger_id: int, redis: Redis = Depends(get_redis_client)):
    try:
        key = f"passenger:{passenger_id}:location"
        passenger_location = await redis.get(key)
        if not passenger_location:
            return {"message": "Passenger's location not found"}
        return {"passenger_id": passenger_id, "location": json.loads(passenger_location)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch passenger location: {str(e)}")

@router.delete("/driver/{driver_id}")
async def delete_driver_location(driver_id: int, redis: Redis = Depends(get_redis_client)):
    try:
        key = f"driver:{driver_id}:location"
        deleted = await redis.delete(key)
        if deleted:
            return {"message": f"Driver's location with ID {driver_id} deleted successfully"}
        return {"message": f"Driver's location with ID {driver_id} not found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete driver location: {str(e)}")

@router.delete("/passenger/{passenger_id}")
async def delete_passenger_location(passenger_id: int, redis: Redis = Depends(get_redis_client)):
    try:
        key = f"passenger:{passenger_id}:location"
        deleted = await redis.delete(key)
        if deleted:
            return {"message": f"Passenger's location with ID {passenger_id} deleted successfully"}
        return {"message": f"Passenger's location with ID {passenger_id} not found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete passenger location: {str(e)}")

@router.get("/passengers/nearby-drivers/{passenger_id}")
async def get_nearby_drivers(passenger_id: int, latitude: float, longitude: float, redis: Redis = Depends(get_redis_client)):
    try:
        passenger_coords = (latitude, longitude)
        drivers_nearby = []
        driver_keys = await redis.keys("driver:*:location")

        for driver_key in driver_keys:
            driver_location = await redis.get(driver_key)
            if not driver_location:
                continue
            driver_location = json.loads(driver_location)
            driver_coords = (driver_location["latitude"], driver_location["longitude"])
            distance = geodesic(passenger_coords, driver_coords).kilometers

            if distance <= 5:
                driver_id = driver_key.split(":")[1]
                drivers_nearby.append({"driver_id": driver_id, "location": driver_location})

        return {"drivers": drivers_nearby}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch nearby drivers: {str(e)}")