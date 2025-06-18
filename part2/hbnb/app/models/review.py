from app.models.base_model import BaseModel
from app.models.place import Place
from app.models.user import User

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()

        # Validate required text field
        if not text:
            raise ValueError("Review text is required.")

        # Validate rating between 1 and 5
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5.")

        # Validate place is instance of Place
        if not isinstance(place, Place):
            raise ValueError("Place must be a Place instance.")

        # Validate user is instance of User
        if not isinstance(user, User):
            raise ValueError("User must be a User instance.")

        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
