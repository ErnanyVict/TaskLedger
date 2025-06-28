import requests

def add_task_DB(name, description, package_id):

    url = "http://localhost:5000/taskledger/tasks"
    json = [{
        "description": description,
        "name": name,
        "package_id": package_id,
        "status": "Incompleted"
    }]
    
    print(json)
    resposta = requests.post(url, json=json)
    print(resposta)
