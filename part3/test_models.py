# test_models.py

from app.extensions import db, bcrypt
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity, place_amenities
from flask import Flask

# Set up a test Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use file or ':memory:' for RAM
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.drop_all()  # Drop old tables
    db.create_all()  # Create fresh ones

    # Create a user
    user = User(first_name='Danah', last_name='Test', email='danah@example.com')
    user.hash_password('securepassword')

    db.session.add(user)
    db.session.commit()

    # Create a place
    place = Place(title="Cool Spot", description="Nice place", price=150.0, latitude=24.7136, longitude=46.6753, owner_id=user.id)
    db.session.add(place)
    db.session.commit()

    # Create an amenity
    amenity = Amenity(name="Wi-Fi")
    db.session.add(amenity)
    db.session.commit()

    # Add amenity to place
    place.amenities.append(amenity)
    db.session.commit()

    # Create a review
    review = Review(text="Great experience!", rating=5, user_id=user.id, place_id=place.id)
    db.session.add(review)
    db.session.commit()

    # Check outputs
    print("User:", user.to_dict())
    print("Place:", place.to_dict())
    print("Review:", review.to_dict())
    print("Amenity:", amenity.to_dict())

    # Check password
    print("Password correct?", user.verify_password('securepassword'))
    print("Wrong password?", user.verify_password('wrongpassword'))
