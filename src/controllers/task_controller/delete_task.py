from fastapi.exceptions import HTTPException
from .router import task_router
from ...models import TaskModel

@task_router.delete('/{task_id}', response_model=dict)
def delete_task(task_id: int):
	task = TaskModel.where(id=task_id).first()
	if task:
		try:
			task.delete()
			return { 'message': 'Task deleted' }
		except:
			raise HTTPException(status_code=500, detail='Server error')
	raise HTTPException(status_code=404, detail='Task not found')
