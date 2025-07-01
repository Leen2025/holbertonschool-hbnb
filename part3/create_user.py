from app import db, create_app
from app.models.user import User

app = create_app()
app.app_context().push()

# Create a test user
user = User(
    id="user-100",
    email="danah@example.com",
    password="danah12345",  # If you use password hashing, hash this!
    first_name="Danah",
    last_name="Alshehri",
    is_admin=False 
)
db.session.add(user)
db.session.commit()
print("User created.")
