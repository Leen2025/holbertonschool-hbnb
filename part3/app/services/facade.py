from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.extensions import db


# ---------- User-related services ----------

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


# ---------- Place-related services ----------

def create_place(data):
    try:
        place = Place(
            title=data['title'],
            description=data.get('description', ''),
            price=data['price'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            owner_id=data['owner_id']
        )

        if 'amenities' in data:
            amenities = Amenity.query.filter(Amenity.id.in_(data['amenities'])).all()
            place.amenities = amenities

        db.session.add(place)
        db.session.commit()
        return place.to_dict()

    except Exception as e:
        print(f"Create place failed: {e}")
        raise



def get_place(place_id):
    return Place.query.get(place_id)

def get_all_places():
    return Place.query.all()

def update_place(place_id, data):
    place = get_place(place_id)
    if not place:
        return None

    if 'title' in data:
        place.title = data['title']
    if 'description' in data:
        place.description = data['description']
    if 'price' in data:
        place.price = data['price']
    if 'latitude' in data:
        place.latitude = data['latitude']
    if 'longitude' in data:
        place.longitude = data['longitude']
    if 'amenities' in data:
        amenity_ids = [int(aid) for aid in data['amenities']]
        amenities = Amenity.query.filter(Amenity.id.in_(amenity_ids)).all()
        place.amenities = amenities

    db.session.commit()
    return place

def delete_place(place_id):
    place = get_place(place_id)
    if place:
        db.session.delete(place)
        db.session.commit()
        return True
    return False


# ---------- Amenity helper ----------
def get_amenity(amenity_id):
    return Amenity.query.get(amenity_id)
