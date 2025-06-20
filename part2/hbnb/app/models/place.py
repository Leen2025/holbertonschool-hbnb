from app.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, owner, title, price, latitude, longitude, description="", amenities=None):
        super().__init__()

        if not title or len(title) > 100:
            raise ValueError("Title is required and must be less than 100 characters.")
        if not owner:
            raise ValueError("Owner (User instance) is required.")

        self.title = title
        self.description = description
        self.price = price           # will call the setter below
        self.latitude = latitude     # will call the setter below
        self.longitude = longitude   # will call the setter below
        self.owner = owner
        self.owner_id = owner.id
        self.reviews = []
        self.amenities = amenities if amenities else []

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be a non-negative float.")
        self._price = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if value < -90.0 or value > 90.0:
            raise ValueError("Latitude must be between -90.0 and 90.0.")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if value < -180.0 or value > 180.0:
            raise ValueError("Longitude must be between -180.0 and 180.0.")
        self._longitude = value

    def add_review(self, review):
        """Add a review to this place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to this place."""
        self.amenities.append(amenity)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner": {
                "id": self.owner.id,
                "first_name": self.owner.first_name,
                "last_name": self.owner.last_name,
                "email": self.owner.email
            },
            "amenities": [amenity.to_dict() for amenity in self.amenities],
            "reviews": [review.to_dict() for review in self.reviews]  
        }
