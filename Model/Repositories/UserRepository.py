import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Entities.User import User

import sqlite3
from pathlib import Path

class UserRepository:

    def __init__(self):
        self.ROOT_DIR = Path(__file__).parent.parent.parent
        self.DB_FILE = self.ROOT_DIR / 'DB.sqlite3'
        self.TABLE_NAME = 'Users'
        self.connection = sqlite3.connect(self.DB_FILE)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {self.TABLE_NAME}' 
            '('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'name TEXT,'
            'password TEXT'
            ')'
        )

        self.connection.commit()
        print("Table created")

    def insert(self, list_users):
        insert = (f'INSERT INTO {self.TABLE_NAME} (name, password) VALUES (?, ?)')
        users = [(user.name, user.password) for user in list_users]
        self.cursor.executemany(insert, users)           
        self.connection.commit()
        print("Done")

    def read_all(self) -> list[User]:
        self.cursor.execute(f'SELECT * FROM {self.TABLE_NAME}')
        users_list = []
        
        for row in self.cursor.fetchall():
            user_id, name, password = row
            users_list.append(User(user_id, name, password))

        return users_list
    
    def read_by_id(self, user_id) -> User:
        self.cursor.execute(f'SELECT * FROM {self.TABLE_NAME} WHERE id = {user_id}')
        row = self.cursor.fetchall()
        user_id, name, password = row[0]
        return User(user_id, name, password)

    def delete_by_id(self, user_id) -> User: 
        user_deleted = self.read_by_id(user_id)
        self.cursor.execute(f'DELETE  FROM {self.TABLE_NAME} WHERE id = {user_id}')
        self.connection.commit()
        return user_deleted

    def update_by_id(self, user_id: int, user: User):
        self.cursor.execute(f'UPDATE {self.TABLE_NAME} SET name = ?, password = ? WHERE id = ?',
                            (user.name, user.password, user_id))
        self.connection.commit()
        return user

    def close(self) -> None:
        self.cursor.close()
        self.connection.close()
        

if __name__ == "__main__":

    repository = UserRepository()



    # u1 = User(None, "Ernany Victor", "1234")
    '''u2 = User(None, "Lucas Pareschi", "2409")
    u3 =  User(None, "Carlos Alberto", "1022")
    u4 = User(None, "Maria Yvone", "2025")
    repository.create_table()
    repository.insert([u2, u3, u4])

    user_deleted = repository.delete_by_id(2)
    print(user_deleted)'''

    u1_updated = User(None, 'Ernany Victor', '4321')
    repository.update_by_id(1, u1_updated)
    users_list = repository.read_all()
    for user in users_list:
        print(user)

    

    repository.close()