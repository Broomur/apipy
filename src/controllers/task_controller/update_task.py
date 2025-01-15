from fastapi.exceptions import HTTPException
from .router import task_router
from ...models import TaskModel
from ...schemas import TaskUpdate, TaskResponse

@task_router.put('/{task_id}', response_model=TaskResponse)
def update_task(task_id: int, updated_task: TaskUpdate):
	task = TaskModel.where(id=task_id).first()
	if task:
		try:
			task.update(**updated_task.dict())
			return task
		except:
			raise HTTPException(status_code=500, detail='Server error')
	raise HTTPException(status_code=404, detail='Task not found')
