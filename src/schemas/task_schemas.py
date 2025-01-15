from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    done: bool = False
    user_id: int


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
