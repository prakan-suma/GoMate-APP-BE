from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.driver_document import DriverDocumentCreate, DriverDocumentUpdate, DriverDocumentOut
from services.driver_document import (
    create_driver_document,
    get_all_driver_documents,
    update_driver_document,
    delete_driver_document
)
from database.session import get_db
from typing import List

router = APIRouter(prefix="/v1/driver-documents", tags=["driver-documents"])

@router.post("/", response_model=dict)
def create_driver_document_view(document: DriverDocumentCreate, db: Session = Depends(get_db)):
    return create_driver_document(db, document)

@router.get("/", response_model=List[DriverDocumentOut])
def get_all_driver_documents_view(db: Session = Depends(get_db)):
    return get_all_driver_documents(db)

@router.patch("/{document_id}", response_model=dict)
def update_driver_document_view(document_id: int, document: DriverDocumentUpdate, db: Session = Depends(get_db)):
    return update_driver_document(db, document_id, document)

@router.delete("/{document_id}", response_model=dict)
def delete_driver_document_view(document_id: int, db: Session = Depends(get_db)):
    return delete_driver_document(db, document_id)