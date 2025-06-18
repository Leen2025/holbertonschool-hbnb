from app.models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        super().__init__(**kwargs)

