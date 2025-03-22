from fastapi import FastAPI
<<<<<<< HEAD
from routers import trip, live_tracking, driver_document, price_guideline
=======
from routers import trip, live_tracking, booking
>>>>>>> prakan

app = FastAPI()

app.include_router(trip.router)
app.include_router(live_tracking.router)
<<<<<<< HEAD
app.include_router(driver_document.router)
app.include_router(price_guideline.router)
=======
app.include_router(booking.router)
>>>>>>> prakan
