from flask import Blueprint, request, jsonify
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Repositories.TaskRepository import TaskRepository
from Entities.Task import Task


task_bp = Blueprint('task', __name__)

@task_bp.route('/tasks', methods=['GET'])
def get_task():
    tasks_list = []
            
    repository = TaskRepository()
    tasks = repository.read_all()
            
    for task in tasks:
        tasks_list.append({'id': task.task_id, 'name': task.name, 'description': task.description, 'status': task.status, 'package_id': task.package_id})

    return jsonify(tasks_list)

@task_bp.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    repository = TaskRepository()
            
    task = repository.read_by_id(int(id))
    task_josn = [{'id': task.task_id, 'name': task.name, 'description': task.description, 'status': task.status, 'package_id': task.package_id}]
    return jsonify(task_josn)

@task_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    repository = TaskRepository()

    task_deleted = repository.delete_by_id(int(id))
    task_deleted_json = [{'id': task_deleted.task_id, 'name': task_deleted.name, 'description': task_deleted.description, 'status': task_deleted.status}]
    return jsonify(task_deleted_json)
        
@task_bp.route('/tasks', methods=['POST'])
def insert():
    repository = TaskRepository()
    tasks_list = []
    tasks = request.get_json()

    for task in tasks:
        tasks_list.append(Task(None, task.get('name'), task.get('description'), task.get('status'), task.get('package_id')))

    repository.insert(tasks_list)
    return jsonify(tasks)
        
@task_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_by_id(id):
    repository = TaskRepository()
    task = request.get_json()
    repository.update_by_id(id, Task(None, task.get('name'), task.get('description'), task.get('status')))
    return jsonify(task)        

@task_bp.route('/tasks/package/<int:id>')
def get_by_package(id):
    repository = TaskRepository()
    list_tasks = repository.read_by_package(id)
    tasks = []
    for task in list_tasks:
        tasks.append({'id': task.task_id, 'name': task.name, 'description': task.description,
        'status': task.status, 'package_id': task.package_id}) 
    
    return jsonify(tasks)