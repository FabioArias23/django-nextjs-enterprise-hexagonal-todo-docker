from tasks.domain.repositories import ITaskRepository

class ToggleTaskDoneUseCase:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    def execute(self, task_id):
        task = self.repository.get_by_id(task_id)
        task.done = not task.done
        return self.repository.save(task)