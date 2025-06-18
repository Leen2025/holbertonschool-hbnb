from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

def test_user_creation():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"
    assert user.is_admin is False  # Default
    print("User creation test passed!")

def test_place_creation():
    owner = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com")
    place = Place(title="Cozy Apartment", description="Nice place", price=150.0, latitude=25.0, longitude=45.0, owner=owner)
    assert place.title == "Cozy Apartment"
    assert place.owner.email == "alice.smith@example.com"
    print("Place creation test passed!")

def test_review_creation():
    user = User(first_name="Bob", last_name="Builder", email="bob@example.com")
    place = Place(title="Test Place", description="", price=100.0, latitude=20.0, longitude=40.0, owner=user)
    review = Review(text="Great place!", rating=5, place=place, user=user)
    assert review.text == "Great place!"
    assert review.rating == 5
    assert review.place == place
    assert review.user == user
    print("Review creation test passed!")

def test_amenity_creation():
    amenity = Amenity(name="Wi-Fi")
    assert amenity.name == "Wi-Fi"
    print("Amenity creation test passed!")

if __name__ == "__main__":
    test_user_creation()
    test_place_creation()
    test_review_creation()
    test_amenity_creation()
