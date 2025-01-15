from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    done: bool = False
    user_id: int
    expire_at: datetime | None = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
