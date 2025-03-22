from sqlalchemy.orm import Session
from models.price_guideline import PriceGuideline

def get_price_guidelines(db: Session, skip: int = 0, limit: int = 10):
    return db.query(PriceGuideline).offset(skip).limit(limit).all()