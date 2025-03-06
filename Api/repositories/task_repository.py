from typing import List, Optional
from models.task_model import Task

# Simulación de una base de datos en memoria
tasks_db = []

class TaskRepository:
    def get_all_tasks(self) -> List[Task]:
        return tasks_db

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        return next((task for task in tasks_db if task.id == task_id), None)

    def create_task(self, task: Task) -> Task:
        tasks_db.append(task)
        return task

    def update_task(self, task_id: int, updated_task: Task) -> Optional[Task]:
        task = self.get_task_by_id(task_id)
        if task:
            task.title = updated_task.title
            task.description = updated_task.description
            task.completed = updated_task.completed
        return task

    def delete_task(self, task_id: int) -> Optional[Task]:
        task = self.get_task_by_id(task_id)
        if task:
            tasks_db.remove(task)
        return task