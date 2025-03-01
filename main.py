from fastapi import FastAPI
from routers import trip, live_tracking, driver_document

app = FastAPI()

app.include_router(trip.router)
app.include_router(live_tracking.router)
app.include_router(driver_document.router)