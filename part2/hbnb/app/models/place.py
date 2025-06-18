from app.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        if not title or len(title) > 100:
            raise ValueError("Invalid title")
        if price < 0:
            raise ValueError("Price must be positive")
        if latitude < -90 or latitude > 90:
            raise ValueError("Latitude must be in range")
        if longitude < -180 or longitude > 180:
            raise ValueError("Longitude must be in range")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)
