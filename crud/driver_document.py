from sqlalchemy.orm import Session
from models.driver_document import DriverDocument
from models.user import User
from fastapi import HTTPException
from schemas.driver_document import DriverDocumentCreate, DriverDocumentUpdate

def create_driver_document(db: Session, document: DriverDocumentCreate):
    # Check if the user exists
    user = db.query(User).filter(User.id == document.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if a driver document already exists for this user
    existing_document = db.query(DriverDocument).filter(DriverDocument.user_id == document.user_id).first()
    if existing_document:
        raise HTTPException(status_code=400, detail="Driver document for this user already exists")

    # Create the driver document
    db_document = DriverDocument(**document.dict(), document_status="pending")
    db.add(db_document)
    db.commit()
    db.refresh(db_document)

    # Return the response in the correct format
    return {
        "message": "Driver document added successfully",
        "document_id": db_document.id
    }

def update_driver_document(db: Session, document_id: int, document: DriverDocumentUpdate):
    # Fetch the driver document
    db_document = db.query(DriverDocument).filter(DriverDocument.id == document_id).first()
    if not db_document:
        raise HTTPException(status_code=404, detail="Driver document not found")

    # Update the document status
    for key, value in document.dict(exclude_unset=True).items():
        setattr(db_document, key, value)

    db.commit()
    db.refresh(db_document)

    # Return the response in the correct format
    return {
        "message": "Driver document updated successfully",
        "document_id": db_document.id
    }

def get_driver_document(db: Session, document_id: int):
    db_document = db.query(DriverDocument).filter(DriverDocument.id == document_id).first()
    if not db_document:
        raise HTTPException(status_code=404, detail="Driver document not found")

    return db_document

def get_driver_documents_by_driver_id(db: Session, driver_id: int):
    db_document = db.query(DriverDocument).filter(DriverDocument.user_id == driver_id).all()
    
    if not db_document:
        raise HTTPException(status_code=404, detail="Driver document not found")
    
    return db_document

def get_driver_documents(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DriverDocument).offset(skip).limit(limit).all()

def delete_driver_document(db: Session, document_id: int):
    db_document = db.query(DriverDocument).filter(DriverDocument.id == document_id).first()
    if not db_document:
        raise HTTPException(status_code=404, detail="Driver document not found")

    db.delete(db_document)
    db.commit()

    return {
        "message": "Driver document deleted successfully",
        "document_id": document_id
    }