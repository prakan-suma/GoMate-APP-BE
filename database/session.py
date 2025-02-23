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




