# app/services/facade.py

from app.models.user import User
from app.models.place import Place
from app.repositories.in_memory_repository import InMemoryRepository
from app.models.amenity import Amenity

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()

    # --- User methods ---
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        """Retrieve all users from the repository"""
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        user = self.user_repo.get(user_id)
        if not user:
            return None
        for key, value in user_data.items():
            setattr(user, key, value)
        self.user_repo.update(user_id, user)
        return user

    # --- Amenity methods ---
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            return None
        amenity.update(amenity_data)
        return amenity

    # --- Place methods ---
    def create_place(self, place_data):
        price = place_data.get('price')
        lat = place_data.get('latitude')
        lon = place_data.get('longitude')

        if price is None or price < 0:
            raise ValueError("Invalid price")

        if lat is None or lat < -90 or lat > 90:
            raise ValueError("Invalid latitude")

        if lon is None or lon < -180 or lon > 180:
            raise ValueError("Invalid longitude")

        owner_id = place_data.pop('owner_id', None)
        if not owner_id:
            raise ValueError("Owner ID is required")
        owner = self.user_repo.get(owner_id)
        if not owner:
            raise ValueError("Owner not found")

        amenity_ids = place_data.pop('amenities', [])
        place = Place(owner=owner, **place_data)

        for amenity_id in amenity_ids:
            amenity = self.amenity_repo.get(amenity_id)
            if amenity:
                place.add_amenity(amenity)

        self.place_repo.add(place)
        return place
