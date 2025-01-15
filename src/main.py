from fastapi import FastAPI
from .database import SessionLocal
from .controllers import task_router

app = FastAPI()

app.include_router(task_router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
