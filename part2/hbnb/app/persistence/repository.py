from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        # Validate required fields
        required_fields = ["first_name", "last_name", "email"]
        for field in required_fields:
            if field not in user_data or not user_data[field]:
                raise ValueError(f"Missing required field: {field}")

        # Check if email already exists
        for existing_user in self.user_repo.get_all():  # <-- تعديل هنا
            if existing_user.email == user_data["email"]:
                raise ValueError("Email already exists")

        # Create and store user
        new_user = User(**user_data)
        self.user_repo.add(new_user)  # استخدم add() لحفظ العنصر
        return new_user

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise ValueError("Place not found")
        return place

    def create_place(self, place_data):
        # Required fields
        required_fields = ["title", "price", "latitude", "longitude", "owner_id"]
        for field in required_fields:
            if field not in place_data or not place_data[field]:
                raise ValueError(f"Missing required field: {field}")

        # Validate price
        if place_data["price"] <= 0:
            raise ValueError("Price must be a positive number")

        # Validate latitude and longitude
        if not (-90.0 <= place_data["latitude"] <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0")
        if not (-180.0 <= place_data["longitude"] <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0")

        # Validate owner exists
        owner = self.user_repo.get(place_data["owner_id"])
        if not owner:
            raise ValueError("Owner (user) not found")

        # Create and save the place
        new_place = Place(
            title=place_data["title"],
            description=place_data.get("description", ""),
            price=place_data["price"],
            latitude=place_data["latitude"],
            longitude=place_data["longitude"],
            owner=owner
        )
        self.place_repo.add(new_place)  
        return new_place

