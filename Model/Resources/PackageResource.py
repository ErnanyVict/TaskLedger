from flask import Blueprint, request, jsonify
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Repositories.PackageRepository import PackageRepository
from Repositories.UserRepository import UserRepository
from Entities.Task import Task
from Entities.Package import Package

package_bp = Blueprint('package', __name__)

@package_bp.route('/packages', methods=['GET'])
def get_packages():
    packages_list = []
            
    repository = PackageRepository()
    packages = repository.read_all()
            
    for package in packages:
        packages_list.append({'id': package.package_id, 'name': package.name,
        'description': package.description, 'status': package.status, 'user_id': package.user})

    return jsonify(packages_list)

@package_bp.route('/packages/<int:id>', methods=['GET'])
def get_task_by_id(id):
    repository = PackageRepository()
            
    package = repository.read_by_id(int(id))
    package_josn = [{'id': package.package_id, 'name': package.name, 'description': package.description,
    'status': package.status, 'user_id': package.user }]
    return jsonify(package_josn)

@package_bp.route('/packages/user/<int:id>', methods=['GET'])
def get_by_user(id):
    repository = PackageRepository()
    packages = repository.read_by_user(id)
    package_json = []
    for package in packages:
        package_json.append({'id': package.package_id, 'name': package.name, 'description': package.description,
        'status': package.status, 'user_id': package.user.user_id}) 
    return jsonify(package_json)

@package_bp.route('/packages/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    repository = PackageRepository()

    package_deleted = repository.delete_by_id(int(id))
    task_deleted_json = [{'id': package_deleted.package_id, 'name': package_deleted.name,
    'description': package_deleted.description,
    'status': package_deleted.status, 'user_id': package_deleted.user}]
    return jsonify(task_deleted_json)
        
@package_bp.route('/packages', methods=['POST'])
def insert():
    repository = PackageRepository()
    packages_list = []
    package = request.get_json()
    repository_user = UserRepository()
    user = repository_user.read_by_id(package.get('user_id'))
    packages_list.append(Package(None, package.get('name'),  package.get('description'),
    package.get('status'), user))

    repository.insert(packages_list)
    return jsonify(package)
        
@package_bp.route('/packages/<int:id>', methods=['PUT'])
def update_by_id(id):
        repository = PackageRepository()
        repository_user = UserRepository()
        package = request.get_json()
        user = repository_user.read_by_id(package.get('user_id'))
        repository.update_by_id(id, Package(None, package.get('name'), package.get('description'),
        package.get('status'), user))
        return jsonify(package)

def run(self):
    self.app.run(port=8080, host='localhost', debug=True)