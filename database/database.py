# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # Replace with your MySQL database connection details
# DATABASE_URL = "mysql+pymysql://username:password@localhost/gomate_db"

# # Create engine and session
# engine = create_engine(DATABASE_URL, connect_args={"charset": "utf8mb4"})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# # Dependency to get database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
