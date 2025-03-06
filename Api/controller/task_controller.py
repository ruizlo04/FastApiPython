from fastapi import APIRouter, HTTPException
from typing import List
from models.task_model import Task
from services.task_service import TaskService

router = APIRouter()
service = TaskService()

@router.get("/tasks", response_model=List[Task])
def get_tasks():
    return service.get_all_tasks()

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = service.get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/tasks", response_model=Task)
def create_task(task: Task):
    return service.create_task(task)

@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    task = service.update_task(task_id, updated_task)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    task = service.delete_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task