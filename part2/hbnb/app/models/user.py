# models/user.py

from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        if not first_name or not last_name or not email:
            raise ValueError("first_name, last_name, and email are required")
        if len(first_name) > 50 or len(last_name) > 50:
            raise ValueError("Name fields must be <= 50 characters")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
