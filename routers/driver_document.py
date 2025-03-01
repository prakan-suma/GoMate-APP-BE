from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from schemas.driver_document import DriverDocumentCreate, DriverDocumentUpdate, DriverDocumentOut
from services.driver_document import create_driver_document_service, get_driver_document_service, update_driver_document_service, delete_driver_document_service, get_driver_documents_service
from database.session import get_db
from typing import List

router = APIRouter(prefix="/v1/driver-documents", tags=["driver-documents"])

@router.post("/", response_model=DriverDocumentOut)
def create_driver_document_view(document: DriverDocumentCreate, db: Session = Depends(get_db)):
    return create_driver_document_service(db=db, document=document)

@router.get("/{document_id}", response_model=DriverDocumentOut)
def get_driver_document_view(document_id: int, db: Session = Depends(get_db)):
    document = get_driver_document_service(db=db, document_id=document_id)
    if document:
        return document
    return {"message": "Driver document not found"}

@router.put("/{document_id}", response_model=DriverDocumentOut)
def update_driver_document_view(document_id: int, document: DriverDocumentUpdate, db: Session = Depends(get_db)):
    return update_driver_document_service(db=db, document_id=document_id, document=document)

@router.delete("/{document_id}")
def delete_driver_document_view(document_id: int, db: Session = Depends(get_db)):
    if delete_driver_document_service(db, document_id):
        return {"message": "Driver document deleted successfully"}
    return {"message": "Driver document not found"}

@router.get("/", response_model=List[DriverDocumentOut])
def get_driver_documents_view(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_driver_documents_service(db, skip, limit)