from fastapi import FastAPI
from routers import trip, booking

app = FastAPI()

# รวม router ที่สร้างขึ้น
app.include_router(trip.router)
app.include_router(booking.router)
