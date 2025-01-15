from fastapi.exceptions import HTTPException
from ...models import TaskModel
from ...schemas import TaskResponse
from .router import task_router

@task_router.get('/detail/{task_id}', response_model=TaskResponse)
def read_task(task_id: int):
	task = TaskModel.where(id=task_id).first()
	if task:
		return task
	raise HTTPException(status_code=404, detail='Task not found')
