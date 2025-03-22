from sqlalchemy.orm import Session
from crud.driver_document import create_driver_document, update_driver_document, get_driver_document, get_driver_documents, delete_driver_document,get_driver_documents_by_driver_id
from schemas.driver_document import DriverDocumentCreate, DriverDocumentUpdate
from models.driver_document import DriverDocument

def create_driver_document_service(db: Session, document: DriverDocumentCreate):
    return create_driver_document(db, document)

def update_driver_document_service(db: Session, document_id: int, document: DriverDocumentUpdate):
    return update_driver_document(db, document_id, document)

def get_driver_document_service(db: Session, document_id: int):
    return get_driver_document(db, document_id)

def get_driver_documents_by_driver_id_service(db: Session, driver_id: int):
    return get_driver_documents_by_driver_id(db, driver_id)

def get_driver_documents_service(db: Session, skip: int = 0, limit: int = 10):
    return get_driver_documents(db, skip, limit)

def delete_driver_document_service(db: Session, document_id: int):
    return delete_driver_document(db, document_id)

def get_all_driver_documents(db: Session):
    documents = db.query(DriverDocument).all()
    return documents