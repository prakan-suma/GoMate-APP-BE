from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# ตั้งค่าการเชื่อมต่อฐานข้อมูล
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:10456@34.70.67.128:3306/gomate_db"

# สร้าง Engine สำหรับเชื่อมต่อ
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={})

# สร้าง SessionLocal สำหรับการจัดการฐานข้อมูล
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# สร้าง Base สำหรับการสร้าง models
Base = declarative_base()

# ฟังก์ชันที่จะใช้สำหรับการสร้าง session ใหม่
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()








from sqlalchemy.orm import Session
from models import User

def create_user(db: Session, name: str, email: str, password: str, phone_number: str, role: str):
    db_user = User(name=name, email=email, password=password, phone_number=phone_number, role=role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # อัพเดทค่าใน db_user
    return db_user


from sqlalchemy import text
from sqlalchemy.orm import Session

def create_user_raw(db: Session, name: str, email: str, password: str, phone_number: str, role: str):
    sql = """
        INSERT INTO users (name, email, password, phone_number, role)
        VALUES (:name, :email, :password, :phone_number, :role)
    """
    db.execute(text(sql), {'name': name, 'email': email, 'password': password, 'phone_number': phone_number, 'role': role})
    db.commit()
