from fastapi import FastAPI
from routers import trip

app = FastAPI()

# รวม router ที่สร้างขึ้น
app.include_router(trip.router)
