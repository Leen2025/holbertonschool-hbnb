uufrom app.services.facade import HBnBFacade

def test_create_user_and_place():
    facade = HBnBFacade()

    user_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com"
    }
    user = facade.create_user(user_data)
    assert user.first_name == "John"
    assert user.email == "john.doe@example.com"

    place_data = {
        "title": "My Cozy Home",
        "description": "A nice place to stay",
        "price": 150.0,
        "latitude": 40.7128,
        "longitude": -74.0060,
        "owner_id": user.id
    }
    place = facade.create_place(place_data)
    assert place.title == "My Cozy Home"
    assert place.owner.id == user.id

    print("User and Place creation test passed!")

if __name__ == "__main__":
    test_create_user_and_place()
