from app.persistence.repository import InMemoryRepository
from app.models.user import User

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
        for existing_user in self.user_repo.all():
            if existing_user.email == user_data["email"]:
                raise ValueError("Email already exists")

        # Create and store user
        new_user = User(**user_data)
        self.user_repo.save(new_user)
        return new_user
