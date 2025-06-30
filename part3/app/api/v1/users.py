from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'first_name': fields.String(required=True, description="User's first name"),
    'last_name': fields.String(required=True, description="User's last name"),
    'email': fields.String(required=True, description="User's email address"),
    'password': fields.String(required=True, description="User's password")
})

user_update_model = api.model('UserUpdate', {
    'first_name': fields.String(description="User's first name"),
    'last_name': fields.String(description="User's last name"),
    'email': fields.String(description="User's email address"),
})

@api.route('/')
class UserList(Resource):
    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Retrieve all users"""
        users = facade.get_all_users()
        return [
            {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            }
            for user in users
        ], 200

    @api.expect(user_model, validate=True)
    @api.response(201, 'User created successfully')
    @api.response(400, 'Email already registered')
    def post(self):
        """Create a new user"""
        data = api.payload
        existing_user = facade.get_user_by_email(data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        new_user = facade.create_user(data)
        return {
            'id': new_user.id,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email
        }, 201


@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Retrieve user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200

    @api.expect(user_update_model, validate=True)
    @api.response(200, 'User updated successfully')
    @api.response(400, 'You cannot modify email or password')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'User not found')
    @jwt_required()
    def put(self, user_id):
        """Update an existing user (only self)"""
        current_user_id = get_jwt_identity()
        if str(current_user_id) != str(user_id):
            return {'error': 'Unauthorized action'}, 403

        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        data = api.payload

        # Disallow updating email or password
        if 'email' in data or 'password' in data:
            return {'error': 'You cannot modify email or password'}, 400

        updated_user = facade.update_user(user_id, data)
        return {
            'id': updated_user.id,
            'first_name': updated_user.first_name,
            'last_name': updated_user.last_name,
            'email': updated_user.email
        }, 200


verify_model = api.model('VerifyPassword', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@api.route('/verify')
class VerifyPassword(Resource):
    @api.expect(verify_model, validate=True)
    def post(self):
        """Verify user password"""
        data = api.payload
        user = facade.get_user_by_email(data['email'])
        if not user:
            return {'error': 'User not found'}, 404

        if user.verify_password(data['password']):
            return {'message': 'Password is correct'}, 200
        else:
            return {'error': 'Incorrect password'}, 401

@api.route('/<user_id>')
class UserDelete(Resource):
    @api.response(200, 'User deleted successfully')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'User not found')
    @jwt_required()
    def delete(self, user_id):
        """Delete user (only self)"""
        current_user_id = get_jwt_identity()
        if str(current_user_id) != str(user_id):
            return {'error': 'Unauthorized action'}, 403

        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        try:
            facade.delete_user(user_id)
            return {'message': 'User deleted successfully'}, 200
        except Exception as e:
            return {'error': str(e)}, 400
