# tasks/infrastructure/repositories_impl.py
from tasks.domain.repositories import TaskRepository
from tasks.models import Task

class DjangoTaskRepository(TaskRepository):
    def get_all(self):
        return Task.objects.all()

    def get_by_id(self, id: int):
        return Task.objects.get(id=id)

    def save(self, task: Task):
        task.save()
        return task