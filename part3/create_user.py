from app import db, create_app
from app.models.user import User
import os

app = create_app()
app.app_context().push()

# Create tables (creates dev.db if missing)
db.create_all()

# Insert user
user = User(
    id=100,
    email="danah@example.com",
    first_name="Danah",
    last_name="Alshehri",
    is_admin=False
)
# Hash the password properly
user.set_password("danah12345")

db.session.add(user)
db.session.commit()
print("User created.")
