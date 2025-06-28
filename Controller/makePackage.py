import requests, os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.Entities.Package import Package
from Model.Entities.User import User

class MakePackage:
    def __init__(self, user_id):
        self.user_id = user_id
        self.get_datas()

    def get_datas(self):
        self.packages_json = requests.get(f'http://localhost:5000/taskledger/packages/user/{self.user_id}').json()
        
    def get_packages(self):
        packages_list = []

        for package in self.packages_json:
            packages_list.append(Package(package.get('id'), package.get('name'), package.get('description'),
            package.get('status'), User(self.user_id)))
        return packages_list