from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    done: bool


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
