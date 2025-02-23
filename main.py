from fastapi import FastAPI
from routers import trip, live_tracking

app = FastAPI()

app.include_router(trip.router)
app.include_router(live_tracking.router)
