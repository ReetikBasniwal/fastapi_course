from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
# Local Imports
import sys
from .config import settings
# import psycopg2
# from psycopg2 import RealDictCursor
# import time

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'

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

# while True:

#     try:
#         conn = psycopg2.connect(host=DATABASE_HOSTNAME, database=settings.database_name, user=settings.database_username,
#                                 password=settings.database_password, cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error:",error)
#         time.sleep(2)