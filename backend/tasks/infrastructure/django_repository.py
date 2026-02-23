from tasks.domain.repositories import ITaskRepository
from tasks.models import Task

class DjangoTaskRepository(ITaskRepository):
    def get_all(self):
        return Task.objects.all()

    def get_by_id(self, task_id):
        return Task.objects.get(id=task_id)

    def save(self, task):
        task.save()
        return task