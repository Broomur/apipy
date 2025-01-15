from fastapi.exceptions import HTTPException
from .router import task_router
from ...models import TaskModel
from ...schemas import TaskCreate, TaskResponse


@task_router.post('', response_model=TaskResponse)
def create_task(new_task: TaskCreate):
	try:
		task = TaskModel.create(**new_task.dict())
		return task
	except:
		raise HTTPException(status_code=500, detail='Server error')
