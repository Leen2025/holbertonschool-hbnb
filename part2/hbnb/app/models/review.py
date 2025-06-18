from app.models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.place_id = kwargs.get('place_id')
        self.rating = kwargs.get('rating', 0)
        self.comment = kwargs.get('comment', '')
        super().__init__(**kwargs)

