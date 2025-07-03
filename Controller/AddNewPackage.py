import requests

def add_package_DB(name, description, user_id):

    url = "http://localhost:5000/taskledger/packages"
    json = {
        "description": description,
        "name": name,
        "user_id": user_id,
        "status": "Incompleted"
    }
    response = requests.post(url, json=json)
