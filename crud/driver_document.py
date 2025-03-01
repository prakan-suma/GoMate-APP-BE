from sqlalchemy.orm import Session
from models.driver_document import DriverDocument
from schemas.driver_document import DriverDocumentCreate, DriverDocumentUpdate

def create_driver_document(db: Session, document: DriverDocumentCreate):
    db_document = DriverDocument(**document.dict())
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document

def update_driver_document(db: Session, document_id: int, document: DriverDocumentUpdate):
    db_document = db.query(DriverDocument).filter(DriverDocument.id == document_id).first()
    if db_document:
        for key, value in document.dict(exclude_unset=True).items():
            setattr(db_document, key, value)
        db.commit()
        db.refresh(db_document)
    return db_document

def get_driver_document(db: Session, document_id: int):
    return db.query(DriverDocument).filter(DriverDocument.id == document_id).first()

def get_driver_documents(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DriverDocument).offset(skip).limit(limit).all()

def delete_driver_document(db: Session, document_id: int):
    db_document = db.query(DriverDocument).filter(DriverDocument.id == document_id).first()
    if db_document:
        db.delete(db_document)
        db.commit()
        return True
    return False