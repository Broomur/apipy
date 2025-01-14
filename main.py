from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, crud
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/tasks")
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)


@app.post("/tasks")
def create_task(title: str, db: Session = Depends(get_db)):
    return crud.create_task(db, title=title)


@app.put("/tasks/{task_id}")
def update_task(task_id: int, title: str, done: bool, db: Session = Depends(get_db)):
    task = crud.update_task(db, task_id, title, done)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
