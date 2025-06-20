from app.models.base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()

        if not name:
            raise ValueError("Amenity name is required")
        if len(name) > 50:
            raise ValueError("Amenity name must be 50 characters or fewer")

        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
