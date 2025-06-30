from app.models.user import User
from app.persistence.repository import SQLAlchemyRepository

class UserRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(User)

    def get_user_by_email(self, email):
        """Get user by email address"""
        return self.model.query.filter_by(email=email).first()

    def email_exists(self, email):
        """Check if email already exists in database"""
        return self.model.query.filter_by(email=email).count() > 0
    def update_user(self, user_id, update_data):
    user = self.get(user_id)
    for key, value in update_data.items():
        if key == 'password':
            user.hash_password(value)
        else:
            setattr(user, key, value)
    self.commit()
    return user

    def delete_user(self, user_id):
        user = self.get(user_id)
        self.delete(user)
        return True
