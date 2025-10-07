from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import sys
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    
    # Test the connection
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

except SQLAlchemyError as e:
    print(f"Database connection error: {e}")
    sys.exit(1)  # Exit if database connection fails

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()