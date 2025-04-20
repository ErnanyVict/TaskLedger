import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Entities.Task import Task

import sqlite3
from pathlib import Path

class TaskRepository:

    def __init__(self):
        self.ROOT_DIR = Path(__file__).parent.parent.parent
        self.DB_FILE = self.ROOT_DIR / 'DB.sqlite3'
        self.TABLE_NAME = 'Task'
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
            'status TEXT'
            ')'
        )

        self.connection.commit()
        print("Table created")

    def insert(self, list_tasks: list[Task]):
        insert = (f'INSERT INTO {self.TABLE_NAME} (name, description, status) VALUES (?, ?, ?)')
        tasks = [(task.name, task.description, task.status) for task in list_tasks]
        self.cursor.executemany(insert, tasks)           
        self.connection.commit()
        print("Done")

    def read_all(self) -> list[Task]:
        self.cursor.execute(f'SELECT * FROM {self.TABLE_NAME}')
        tasks_list = []
        
        for row in self.cursor.fetchall():
            task_id, name, description, status = row
            tasks_list.append(Task(task_id, name, description, status))

        return tasks_list
    
    def read_by_id(self, task_id) -> Task:
        self.cursor.execute(f'SELECT * FROM {self.TABLE_NAME} WHERE id = {task_id}')
        row = self.cursor.fetchall()
        task_id, name, description, status = row[0]
        return Task(task_id, name, description, status)

    def delete_by_id(self, task_id) -> Task: 
        task_deleted = self.read_by_id(task_id)
        self.cursor.execute(f'DELETE  FROM {self.TABLE_NAME} WHERE id = {task_id}')
        self.connection.commit()
        return task_deleted

    def update_by_id(self, task_id: int, task: Task):
        self.cursor.execute(f'UPDATE {self.TABLE_NAME} SET name = ?, description = ?, status = ? WHERE id = ?',
                            (task.name, task.description, task.status, task_id))
        self.connection.commit()
        return task

    def close(self) -> None:
        self.cursor.close()
        self.connection.close()
        

if __name__ == "__main__":

    repository = TaskRepository()

    # repository.create_table()

    t1 = Task(None, "Ir ao banheiro", "Quero fazer ainda hoje isso :D", "Completed")
    t2 = Task(None, "Dr. Stone", "Terminar de assistir Dr. Stone ep 2 a 5", "Incomplete")
    t3 = Task(None, "Dormir", "Vou dormir hoje até umas 3 hrs", "Incomplete")
    repository.insert([t1, t2, t3])

    tasks = repository.read_all()
    for t in tasks:
        print(t)

    print(repository.read_by_id(1))

    t1_modified = t1
    t1_modified.status = "Incompleted" 
    repository.update_by_id(1, t1_modified)

    #repository.delete_by_id(2)
    ts = repository.read_all()
    for t in ts:
        print(t)
    

    repository.close()