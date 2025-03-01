from sqlalchemy.orm import Session
from crud.price_guideline import get_price_guidelines
from schemas.price_guideline import PriceGuidelineOut
from typing import List

def get_price_guidelines_service(db: Session, skip: int = 0, limit: int = 10) -> List[PriceGuidelineOut]:
    guidelines = get_price_guidelines(db, skip, limit)
    # Convert SQLAlchemy models to Pydantic models
    return [PriceGuidelineOut.model_validate(guideline) for guideline in guidelines]