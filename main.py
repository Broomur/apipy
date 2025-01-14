from fastapi import FastAPI, HTTPException
from . import models, schemas
from .database import engine, SessionLocal
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/tasks", response_model=List[schemas.TaskResponse])
def read_tasks():
    return models.TaskModel.all()


@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def read_task(task_id: int):
    task = models.TaskModel.where(id=task_id).first()
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(new_task: schemas.TaskCreate):
    task = models.TaskModel.create(title=new_task.title, done=new_task.done)
    return task


@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, updated_task: schemas.TaskCreate):
    task = models.TaskModel.where(id=task_id).first()
    if task:
        task.update(title=updated_task.title, done=updated_task.done)
        return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task = models.TaskModel.where(id=task_id).first()
    if task:
        task.delete()
        return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
