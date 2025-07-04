import requests

def delete_package(id_package):
    url = f"http://localhost:5000/taskledger/packages/{id_package}"
    response = requests.delete(url)