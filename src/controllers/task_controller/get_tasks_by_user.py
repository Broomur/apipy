from typing import List
from .router import task_router
from ...models import TaskModel
from ...schemas import TaskResponse

@task_router.get('/user/{user_id}', response_model=List[TaskResponse])
def get_tasks_by_user(user_id: int):
	return TaskModel.where(user_id=user_id).all()
