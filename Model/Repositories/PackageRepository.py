import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Model.Entities.Task import Task
from Model.Entities.Package import Package
from Model.Repositories.UserRepository import UserRepository

import sqlite3
from pathlib import Path

class PackageRepository:

    def __init__(self):
        self.ROOT_DIR = Path(__file__).parent.parent.parent
        self.DB_FILE = self.ROOT_DIR / 'DB.sqlite3'
        self.TABLE_NAME = 'ListsTask'
        self.connection = sqlite3.connect(self.DB_FILE)
        self.cursor = self.connection.cursor()

    def delete_all(self):
        self.cursor.execute(f'DELETE FROM {self.TABLE_NAME}')
        self.cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{self.TABLE_NAME}"')
        self.connection.commit()
        print("Table delete")

    def create_table(self):
        self.cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {self.TABLE_NAME}' 
            '('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'name TEXT,'
            'description TEXT,'
            'status TEXT,'
            'user_id INTEGER,'
            'FOREIGN KEY(user_id) REFERENCES User(id)'
            ')'
        )

        self.connection.commit()
        print("Table created")

    def insert(self, packages_list: list[Package]):
        insert = (f'INSERT INTO {self.TABLE_NAME} (name, description, status, user_id) VALUES (?, ?, ?, ?)')
        packages = [(package.name, package.description, package.status, package._user.user_id) for package in packages_list]
        self.cursor.executemany(insert, packages)           
        self.connection.commit()
        print("Done")

    def read_all(self) -> list[Package]:
        self.cursor.execute(f'SELECT * FROM {self.TABLE_NAME}')
        packages = []
        
        for row in self.cursor.fetchall():
            package_id, package_name, package_description, package_status, package_user = row
            packages.append(Package(package_id, package_name, package_description, package_status, package_user))

        return packages
    
    def read_by_id(self, package_id) -> Package:
        self.cursor.execute(f'SELECT * FROM {self.TABLE_NAME} WHERE id = {package_id}')
        row = self.cursor.fetchall()
        p_id, name, description, status, user_id = row[0]
        return Package(package_id, name, description, status, user_id)

    def delete_by_id(self, package_id) -> Package: 
        package_deleted = self.read_by_id(package_id)
        self.cursor.execute(f'DELETE  FROM {self.TABLE_NAME} WHERE id = {package_id}')
        self.connection.commit()
        return package_deleted

    def update_by_id(self, package_id: int, package: Package):
        self.cursor.execute(f'UPDATE {self.TABLE_NAME} SET name = ?, description = ?, status = ?, user_id = ? WHERE id = ?',
                            (package.name, package.description, package.status, package.user.user_id, package_id))
        self.connection.commit()
        return package

    def close(self) -> None:
        self.cursor.close()
        self.connection.close()
        

if __name__ == "__main__":

    repository = PackageRepository()
    # repository.create_table()
    repository_user = UserRepository()
    users = repository_user.read_all()
    for u in users:
        print(u)


    '''p1 = Package(None, "20/04", "tudo isso tem que ser feito no dia 20 de Abril", "Incomplete", users[0])
    p2 = Package(None, "21/04", "...", "Incomplete", users[1])
    p3 = Package(None, "05/2025", "Tudo que tem que ser feito mês que vem", "Incomplete", users[0])
    repository.insert([p1, p2, p3])'''

    p3_update = Package(None, "05/2025", "Tudo que tem que ser feito mês que vem", " Completed", users[0])
    repository.update_by_id(3, p3_update)
    repository.delete_by_id(8)

    ps = repository.read_all()
    for p in ps:
        print(p)

    print(repository.read_by_id(1))

    '''t1_modified = t1
    t1_modified.status = "Incompleted" 
    repository.update_by_id(1, t1_modified)

    #repository.delete_by_id(2)
    ts = repository.read_all()
    for t in ts:
        print(t)
    '''

    repository.close()