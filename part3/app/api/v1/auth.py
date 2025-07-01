from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.services import facade
import logging

api = Namespace('auth', description='Authentication operations')

login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password'),
})

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        credentials = api.payload
        email = credentials.get('email')
        password = credentials.get('password')

        if not email or not password:
            return {'error': 'Email and password required'}, 400

        user = facade.get_user_by_email(email)
        if not user:
            return {'error': 'Invalid credentials'}, 401

        try:
            if not user.verify_password(password):
                return {'error': 'Invalid credentials'}, 401
        except Exception as e:
            logging.error(f"Password verification failed: {e}")
            return {'error': 'Internal Server Error'}, 500

        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"is_admin": user.is_admin}
        )

        return {
            'access_token': access_token,
            'user': {
                'id': user.id,
                'email': user.email,
                'is_admin': user.is_admin
            }
        }, 200
