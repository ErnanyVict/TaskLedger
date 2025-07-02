import requests

def delete_task(id_task):
    url = f"http://localhost:5000/taskledger/tasks/{id_task}"
    response = requests.delete(url)
    print(response) 