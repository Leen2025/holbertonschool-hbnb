from app import create_app
from app.extensions import db
from app.models.user import User

app = create_app()
app.app_context().push()

user = User.query.filter_by(email="danah@example.com").first()
if user:
    print(f"Before fix: {user.password}")
    user.set_password("danah12345")  # Hash the plaintext password properly
    db.session.commit()
    print(f"After fix: {user.password}")
else:
    print("User not found.")
