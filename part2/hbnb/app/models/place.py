from app.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()

        if not title or len(title) > 100:
            raise ValueError("Title is required and must be less than 100 characters.")
        if price <= 0:
            raise ValueError("Price must be a positive number.")
        if latitude < -90.0 or latitude > 90.0:
            raise ValueError("Latitude must be between -90.0 and 90.0.")
        if longitude < -180.0 or longitude > 180.0:
            raise ValueError("Longitude must be between -180.0 and 180.0.")
        if not owner:
            raise ValueError("Owner (User instance) is required.")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner  # User instance
        self.reviews = []  # Related reviews
        self.amenities = []  # Related amenities

    def add_review(self, review):
        """Add a review to this place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to this place."""
        self.amenities.append(amenity)
