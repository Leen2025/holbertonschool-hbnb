from app.services.repositories.user_repository import UserRepository
from app.models.user import User

class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()

    def create_user(self, user_data):
        """Create a new user"""
        if self.user_repo.email_exists(user_data['email']):
            raise ValueError("Email already exists")

        user = User(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=user_data['email'],
            is_admin=user_data.get('is_admin', False)
        )
        user.hash_password(user_data['password'])
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Get user by ID"""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """Get user by email"""
        return self.user_repo.get_user_by_email(email)

    def authenticate_user(self, email, password):
        """Authenticate user"""
        user = self.get_user_by_email(email)
        if user and user.verify_password(password):
            return user
        return None

    def update_user(self, user_id, update_data):
        return self.user_repo.update_user(user_id, update_data)

    def delete_user(self, user_id):
        return self.user_repo.delete_user(user_id)
