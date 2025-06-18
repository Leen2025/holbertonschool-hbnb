from app.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.address = kwargs.get('address')
        self.city = kwargs.get('city')
        self.price_per_night = kwargs.get('price_per_night', 0)
        self.owner_id = kwargs.get('owner_id')  # علاقة بمستخدم
        self.amenities = kwargs.get('amenities', [])  # علاقة بأشياء
        self.reviews = []  # قائمة بالتقييمات
        super().__init__(**kwargs)

    def add_amenity(self, amenity_id):
        if amenity_id not in self.amenities:
            self.amenities.append(amenity_id)

    def add_review(self, review):
        self.reviews.append(review)

