from fastapi import FastAPI
import psycopg2
# Local Imports
from . import models
from .database import engine
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# while True:

#     try:
#         conn = psycopg2.connect(host='127.0.0.1', database='fastapi', user='postgres',
#                                 password='Reetik@2001', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error:",error)
#         time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)