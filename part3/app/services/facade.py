from app.models.user import User
from app.extensions import db

def get_all_users():
    return User.query.all()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_user(user_id):
    return User.query.get(user_id)

def create_user(data):
    user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email']
    )
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return user

def update_user(user_id, data):
    user = get_user(user_id)
    if not user:
        return None
    if 'first_name' in data:
        user.first_name = data['first_name']
    if 'last_name' in data:
        user.last_name = data['last_name']
    if 'email' in data:
        user.email = data['email']
    db.session.commit()
    return user
from app.models.place import Place
from app.models.amenity import Amenity

def create_place(data):
    place = Place(
        title=data['title'],
        description=data.get('description', ''),
        price=data['price'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        owner_id=data['owner_id']
    )

    # Add amenities if provided
    if 'amenities' in data:
        amenities = Amenity.query.filter(Amenity.id.in_(data['amenities'])).all()
        place.amenities = amenities

    db.session.add(place)
    db.session.commit()
    return place.to_dict()
