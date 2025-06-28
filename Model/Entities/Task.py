class Task:
    def __init__(self, task_id: int = None, name: str = None,
        description: str = None, status = "Incomplete", package_id: int = None) -> None:
        self._task_id: int =  task_id
        self._name: str = name
        self._description: str = description
        self._status: str = status
        self._package_id: int = package_id
    
    @property    
    def task_id(self) -> int:
        return self._task_id

    @property    
    def name(self) -> str:
        return self._name
    
    @property    
    def description(self) -> str:
        return self._description
    
    @property    
    def status(self) -> str:
        return self._status

    @task_id.setter
    def task_id(self, user_id) -> None:
        self._task_id = user_id

    @name.setter
    def name(self, name) -> None:
        self._name = name

    @description.setter
    def description(self, description) -> None:
        self._description = description

    @status.setter
    def status(self, status) -> None:
        self._status = status

    @property    
    def package_id(self) -> int:
        return self._package_id

    @package_id.setter
    def package_id(self, status) -> None:
        self._status = status


    def __str__(self):
        return f"(id: {self.task_id}, name: {self.name}," \
        f"description: {self.description}, status: {self.status}, package_id: {self.package_id})"