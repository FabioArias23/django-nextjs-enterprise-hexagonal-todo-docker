# backend/tasks/application/task_service.py
from backend.tasks.domain.repositories import ITaskRepository


class TaskService:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    def toggle_task(self, task_id: int):
        # Lógica Senior: Validaciones antes de ejecutar
        return self.repository.update_status(task_id)