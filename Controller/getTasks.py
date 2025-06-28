import sys, os, requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from json import loads
from Model.Entities.Task import Task
def get_tasks(numPackage):
    tasks = requests.get(f'http://localhost:5000/taskledger/tasks/package/{numPackage}')
    tasks_json = loads(tasks.text)
    tasks_list = [Task(task.get('id'), task.get('name'), task.get('description'), task.get('status'), task.get('package_id')) for task in tasks_json]
    print(tasks.text)
    return tasks_list