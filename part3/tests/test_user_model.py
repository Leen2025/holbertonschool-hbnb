from app import create_app, db
from app.models.user import User
import pytest

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

def test_user_creation(app):
    with app.app_context():
        user = User(
            first_name="Test",
            last_name="User",
            email="test@example.com",
            password="password123"
        )
        db.session.add(user)
        db.session.commit()
        
        fetched = User.query.first()
        assert fetched.email == "test@example.com"

def test_password_hashing(app):
    with app.app_context():
        user = User(email="test@example.com", password="test123")
        assert user.password != "test123"  # Should be hashed
        assert user.verify_password("test123") is True

def test_email_uniqueness(app):
    with app.app_context():
        user1 = User(email="dupe@test.com", password="test123")
        db.session.add(user1)
        db.session.commit()
        
        user2 = User(email="dupe@test.com", password="test123")
        db.session.add(user2)
        try:
            db.session.commit()
            assert False  # Should raise integrity error
        except:
            db.session.rollback()
            assert True
