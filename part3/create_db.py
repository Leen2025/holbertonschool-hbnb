from app.extensions import db
from app import create_app


from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.models.place_amenity import place_amenities

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Tables created successfully!")
