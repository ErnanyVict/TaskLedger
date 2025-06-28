import requests, sys, os
from json import loads
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.Entities.User import User

class EnterAccount:
    def __init__(self, name_txt: str = None, password_txt: str = None):
        self.name_txt = name_txt.capitalize()
        self.password_txt = password_txt
        self.user = None

    def get_datas_DB(self):
        x = requests.get('http://localhost:5000/taskledger/users')
        self.users_json =  loads(x.text)
        self.users_list = [User(user.get('id'), user.get('name'), user.get('password')) for user in self.users_json]
    def compare_name(self):
        for user in self.users_list:
            if user.name.capitalize() == self.name_txt:
                self.user = user
            return self.user
        
        print(f"!! {self.name_txt} != {self.names_db}")
        return None
    
    def compare_password(self):
        self.password_db = self.user.password
        if  self.password_txt == self.password_db:
                return True
        
        print(self.user)
        print(f"!! {self.password_txt} != {self.password_db}")
        return False
    
    def enter(self):
        self.get_datas_DB()
        user = self.compare_name()
        if user == None:
            return self.user
        else:
            if self.compare_password():
                return self.user
                
    
if __name__ == '__main__':
    ea = EnterAccount()
    ea.get_datas_DB()
