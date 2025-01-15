from fastapi import APIRouter

task_router = APIRouter(
	prefix='/tasks',
	tags=['tasks'],
	responses={ 404: { 'description': 'Task not found' } }
)
