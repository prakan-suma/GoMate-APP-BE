from fastapi import APIRouter, Depends
from database.redis import redis_client
import json
from geopy.distance import geodesic

router = APIRouter(prefix="/v1/live-tracking", tags=["live-tracking"])


@router.post("/driver/{driver_id}")
async def update_driver_location_view(driver_id: int, location: dict):
    key = f"driver:{driver_id}:location"
    await redis_client.set(key, json.dumps(location))
    return {"message": "Driver's location update successfully"}


@router.post("/passenger/{passenger_id}")
async def update_passenger_location_view(passenger_id: int, location: dict):
    key = f"passenger:{passenger_id}:location"
    await redis_client.set(key, json.dumps(location))
    return {"message": "Passenger's location update successfully"}


@router.get("/drivers")
async def get_all_drivers():
    driver_keys = await redis_client.keys("driver:*:location")
    drivers = []

    for driver_key in driver_keys:
        driver_location = await redis_client.get(driver_key)
        if driver_location:
            driver_location = json.loads(driver_location)
            driver_id = driver_key.split(":")[1]
            driver = {
                "driver_id": driver_id,
                "location": driver_location
            }
            drivers.append(driver)

    return {"drivers": drivers}


@router.get("/passengers")
async def get_all_passengers():
    passenger_keys = await redis_client.keys("passenger:*:location")
    passengers = []

    for passenger_key in passenger_keys:
        passenger_location = await redis_client.get(passenger_key)
        if passenger_location:
            passenger_location = json.loads(passenger_location)
            passenger_id = passenger_key.split(":")[1]
            passenger = {
                "passenger_id": passenger_id,
                "location": passenger_location
            }
            passengers.append(passenger)

    return {"passengers": passengers}


@router.get("/driver/{driver_id}")
async def get_driver_location(driver_id: int):
    key = f"driver:{driver_id}:location"
    driver_location = await redis_client.get(key)
    if not driver_location:
        return {"message": "Driver's location not found"}
    return {"driver_id": driver_id, "location": json.loads(driver_location)}


@router.get("/passenger/{passenger_id}")
async def get_passenger_location(passenger_id: int):
    key = f"passenger:{passenger_id}:location"
    passenger_location = await redis_client.get(key)
    if not passenger_location:
        return {"message": "Passenger's location not found"}
    return {"passenger_id": passenger_id, "location": json.loads(passenger_location)}


@router.delete("/driver/{driver_id}")
async def delete_driver_location(driver_id: int):
    key = f"driver:{driver_id}:location"
    deleted = await redis_client.delete(key)
    if deleted:
        return {"message": f"Driver's location with ID {driver_id} deleted successfully"}
    return {"message": f"Driver's location with ID {driver_id} not found"}


@router.delete("/passenger/{passenger_id}")
async def delete_passenger_location(passenger_id: int):
    key = f"passenger:{passenger_id}:location"
    deleted = await redis_client.delete(key)
    if deleted:
        return {"message": f"Passenger's location with ID {passenger_id} deleted successfully"}
    return {"message": f"Passenger's location with ID {passenger_id} not found"}


@router.get("/passengers/nearby-drivers/{passenger_id}")
async def get_nearby_drivers(passenger_id: int, latitude: float, longitude: float):
    passenger_coords = (latitude, longitude)

    drivers_nearby = []

    driver_keys = await redis_client.keys("driver:*:location")

    for driver_key in driver_keys:
        driver_location = await redis_client.get(driver_key)

        if not driver_location:
            continue

        driver_location = json.loads(driver_location)
        driver_coords = (
            driver_location["latitude"], driver_location["longitude"])

        distance = geodesic(passenger_coords, driver_coords).kilometers

        if distance <= 5:
            driver_id = driver_key.split(":")[1]
            driver = {
                "driver_id": driver_id,
                "location": driver_location
            }
            drivers_nearby.append(driver)

    return {"drivers": drivers_nearby}
