from app import create_app
from app.services import facade

app = create_app()
app.app_context().push()

user_data = {
    "first_name": "Danah",
    "last_name": "Alshehri",
    "email": "danah@example.com",
    "password": "danah12345"
}

user = facade.create_user(user_data)
print(f"User created with id: {user.id}")
