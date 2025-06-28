from flask import Blueprint, request, jsonify
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Repositories.UserRepository import UserRepository
from Entities.User import User

user_bp = Blueprint('user', __name__)


@user_bp.route('/users', methods=['GET'])
def get_user():
    users_list = []
            
    repository = UserRepository()
    users = repository.read_all()
            
    for user in users:
        users_list.append({'id': user.user_id, 'name': user.name, 'password': user.password})

    return jsonify(users_list)

@user_bp.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    repository = UserRepository()
            
    user = repository.read_by_id(int(id))
    user_josn = [{'id': user.user_id, 'name': user.name, 'password': user.password}]
    return jsonify(user_josn)

@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    repository = UserRepository()

    user_deleted = repository.delete_by_id(int(id))
    user_deleted_json = [{'id': user_deleted.user_id, 'name': user_deleted.name, 'password': user_deleted.password}]
    return jsonify(user_deleted_json)
        
@user_bp.route('/users', methods=['POST'])
def insert():
    repository = UserRepository()
    users_list = []
    users = request.get_json()
    for user in users:
        users_list.append(User(None, user.get('name'), user.get('password')))

    repository.insert(users_list)
    return jsonify(user)
        
@user_bp.route('/users/<int:id>', methods=['PUT'])
def update_by_id(id):
    repository = UserRepository()
    user = request.get_json()
    repository.update_by_id(id, User(None, user.get('name'), user.get('password')))
    return jsonify(user)
