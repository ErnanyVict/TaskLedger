from flask import Flask, request, jsonify
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Repositories.TaskRepository import TaskRepository
from Entities.Task import Task

class TaskResource:
    def __init__(self):
        self.app = Flask(__name__)

    def setup_routes(self):

        @self.app.route('/tasks', methods=['GET'])
        def get_task():
            tasks_list = []
            
            repository = TaskRepository()
            tasks = repository.read_all()
            
            for task in tasks:
                tasks_list.append({'id': task.task_id, 'name': task.name, 'description': task.description, 'status': task.status})

            return jsonify(tasks_list)

        @self.app.route('/tasks/<int:id>', methods=['GET'])
        def get_task_by_id(id):
            repository = TaskRepository()
            
            task = repository.read_by_id(int(id))
            task_josn = [{'id': task.task_id, 'name': task.name, 'description': task.description, 'status': task.status}]
            return jsonify(task_josn)

        @self.app.route('/tasks/<int:id>', methods=['DELETE'])
        def delete_by_id(id):
            repository = TaskRepository()

            task_deleted = repository.delete_by_id(int(id))
            task_deleted_json = [{'id': task_deleted.task_id, 'name': task_deleted.name, 'description': task_deleted.description, 'status': task_deleted.status}]
            return jsonify(task_deleted_json)
        
        @self.app.route('/tasks', methods=['POST'])
        def insert():
            repository = TaskRepository()
            tasks_list = []
            tasks = request.get_json()

            for task in tasks:
                tasks_list.append(Task(None, task.get('name'), task.get('description'), task.get('status')))

            repository.insert(tasks_list)
            return jsonify(tasks)
        
        @self.app.route('/tasks/<int:id>', methods=['PUT'])
        def update_by_id(id):
            print("oi")
            repository = TaskRepository()
            task = request.get_json()
            print(task)
            repository.update_by_id(id, Task(None, task.get('name'), task.get('description'), task.get('status')))
            return jsonify(task)



    def run(self):
        self.app.run(port=8080, host='localhost', debug=True)
        
if __name__ == '__main__':
    UR = TaskResource()
    UR.setup_routes()
    UR.run()