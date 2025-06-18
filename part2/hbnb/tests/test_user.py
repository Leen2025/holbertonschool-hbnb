from models.user import User

def test_user():
    user = User("Leen", "Alsaleh", "leen@example.com")
    assert user.first_name == "Leen"
    assert user.last_name == "Alsaleh"
    assert user.email == "leen@example.com"
    assert user.is_admin is False
    print("✅ User test passed")

test_user()
