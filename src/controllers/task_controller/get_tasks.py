from typing import List
from .router import task_router
from ...models import TaskModel
from ...schemas import TaskResponse


@task_router.get('', response_model=List[TaskResponse])
def get_tasks():
	return TaskModel.all()
