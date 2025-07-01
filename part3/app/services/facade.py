from app.models.user import User
from app.extensions import db

def get_all_users():
    return User.query.all()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_user(user_id):
    return User.query.get(user_id)

def create_user(data):
    user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email']
    )
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return user

def update_user(user_id, data):
    user = get_user(user_id)
    if not user:
        return None
    if 'first_name' in data:
        user.first_name = data['first_name']
    if 'last_name' in data:
        user.last_name = data['last_name']
    if 'email' in data:
        user.email = data['email']
    db.session.commit()
    return user
