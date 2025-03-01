from pydantic import BaseModel
from datetime import datetime

class DriverDocumentBase(BaseModel):
    user_id: int
    license_number: str
    vehicle_registration: str
    vehicle_brand: str
    vehicle_model: str
    vehicle_color: str

class DriverDocumentCreate(DriverDocumentBase):
    pass

class DriverDocumentUpdate(BaseModel):
    document_status: str

class DriverDocumentOut(DriverDocumentBase):
    id: int
    document_status: str
    created_at: datetime

    class Config:
        orm_mode = True