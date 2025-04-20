class User:
    def __init__(self, user_id: int = None, name: str = None, password: str = None) -> None:
        self._user_id: int =  user_id
        self._name: str = name
        self._password: str = password

    @property    
    def user_id(self) -> int:
        return self._user_id

    @property    
    def name(self) -> str:
        return self._name
    
    @property    
    def password(self) -> str:
        return self._password

    @user_id.setter
    def _id(self, user_id) -> None:
        self._user_id = user_id

    @name.setter
    def name(self, name) -> None:
        self._name = name

    @password.setter
    def password(self,  password) -> None:
        self._password = password

    def __str__(self):
        return f"(id: {self.user_id}, name: {self.name}, password: {self.password})"