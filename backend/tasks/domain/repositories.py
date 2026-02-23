from abc import ABC, abstractmethod

class ITaskRepository(ABC):
    @abstractmethod
    def get_all(self): pass
    
    @abstractmethod
    def get_by_id(self, id): pass

    @abstractmethod
    def save(self, task): pass