from typing import List, Optional
from models.task_model import Task
from repositories.task_repository import TaskRepository

class TaskService:
    def __init__(self):
        self.repository = TaskRepository()

    def get_all_tasks(self) -> List[Task]:
        return self.repository.get_all_tasks()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        return self.repository.get_task_by_id(task_id)

    def create_task(self, task: Task) -> Task:
        return self.repository.create_task(task)

    def update_task(self, task_id: int, updated_task: Task) -> Optional[Task]:
        return self.repository.update_task(task_id, updated_task)

    def delete_task(self, task_id: int) -> Optional[Task]:
        return self.repository.delete_task(task_id)