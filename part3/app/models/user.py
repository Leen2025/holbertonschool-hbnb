from app import db, bcrypt
from app.models.base_model import BaseModel
from app import db
import bcrypt
from sqlalchemy import event
from sqlalchemy.orm import validates

class User(BaseModel):
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    @validates('email')
    def validate_email(self, key, email):
        """Validate email format"""
        if '@' not in email:
            raise ValueError("Invalid email address")
        return email

    def hash_password(self, password):
        """Hash the password before storing it"""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verify the hashed password"""
        return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User {self.email}>"

# This ensures password is hashed before saving
@event.listens_for(User, 'before_insert')
def hash_user_password(mapper, connection, target):
    if target.password and not target.password.startswith('$2b$'):
        target.hash_password(target.password)
