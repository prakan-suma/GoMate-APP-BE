# main.py
from fastapi import FastAPI
from routers import trip, live_tracking, driver_document, price_guideline, booking
from database.redis import get_redis, REDIS_HOST, REDIS_PORT
from redis.asyncio import Redis

app = FastAPI()

# Include routers
app.include_router(trip.router)
app.include_router(live_tracking.router)
app.include_router(driver_document.router)
app.include_router(price_guideline.router)
app.include_router(booking.router)

@app.on_event("startup")
async def startup_event():
    # Test Redis connection on startup
    redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    try:
        await redis_client.ping()
        print("Connected to Redis successfully")
    except Exception as e:
        print(f"Failed to connect to Redis: {e}")
    finally:
        await redis_client.close()