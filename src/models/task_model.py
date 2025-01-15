from sqlalchemy import Column, Integer, String, Boolean
from ..database import Base


class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    done = Column(Boolean, nullable=False, default=False)
    user_id = Column(Integer, nullable=False)
