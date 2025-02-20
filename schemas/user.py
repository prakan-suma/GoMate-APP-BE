from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: str
    phone: str
    profile_pic: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    is_driver_active: Optional[bool] = None

class UserOut(UserBase):
    id: int
    is_driver_active: bool
    created_at: datetime

    class Config:
        orm_mode = True
