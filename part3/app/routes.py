from flask import request, jsonify
from app import app
from app.services.facade import HBnBFacade

facade = HBnBFacade()

@app.route('/api/v1/users/', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        user = facade.create_user(data)
        return jsonify({
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/v1/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = facade.get_user(user_id)
    if user:
        return jsonify({
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        })
    return jsonify({'error': 'User not found'}), 404
