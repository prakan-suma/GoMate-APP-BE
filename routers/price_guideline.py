from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.price_guideline import PriceGuidelineOut
from services.price_guideline import get_price_guidelines_service
from database.session import get_db
from typing import List

router = APIRouter(prefix="/v1/price-guidelines", tags=["price-guidelines"])

@router.get("/", response_model=dict)
def get_price_guidelines_view(db: Session = Depends(get_db)):
    guidelines = get_price_guidelines_service(db)
    return {"price_guidelines": guidelines}