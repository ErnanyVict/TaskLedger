import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Model.Entities.Task import Task
from Model.Entities.User import User

class Package:
    def __init__(self, package_id: int = None, name: str = None, description: str = None, status: str = "Incomplete", user: User = None) -> None:
        self._package_id: int =  package_id
        self._name: str = name
        self._description: str = description
        self._status: str = status
        self._list_tasks: list[Task] = []
        self._user = user

    @property    
    def package_id(self) -> int:
        return self._package_id

    @property    
    def name(self) -> str:
        return self._name
    
    @property    
    def description(self) -> str:
        return self._description
    
    @property    
    def status(self) -> str:
        return self._status

    @property    
    def list_tasks(self) -> list[Task]:
        return self._list_tasks
    
    @property    
    def user(self) -> User:
        return self._user

    @package_id.setter
    def package_id(self, package_id) -> None:
        self._package_id = package_id

    @name.setter
    def name(self, name) -> None:
        self._name = name

    @description.setter
    def description(self, description) -> None:
        self._description = description

    @status.setter
    def status(self, status) -> None:
        self._status = status

    @user.setter
    def user(self, user) -> None:
        self._user = user  

    def list_tasks_add(self, task: Task):
        self.list_tasks.append(task)

    def list_tasks_remove(self, task: Task):
        self.list_tasks.remove(task)

    def __str__(self):
        return f"(id: {self.package_id}, name: {self.name}, description: {self.description}, status: {self.status}, user: {self.user})"
    
    def __eq__(self, other: Task) -> bool:
        return self.task_id == other.task_id