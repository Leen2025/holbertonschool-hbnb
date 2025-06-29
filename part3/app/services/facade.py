from app.models.user import User
from app.extensions import db

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()
