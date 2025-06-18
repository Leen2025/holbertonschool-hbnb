from app.models.user import User
from app.models.place import Place

def test_place():
    # def test_place():
    owner = User("Leen", "Alsaleh", "leen@example.com")

    # Create a new place
    place = Place(
        title="Nice Apartment",
        description="Cozy place in the city center",
        price=250.5,
        latitude=24.7136,
        longitude=46.6753,
        owner=owner
    )

    # Check values
    assert place.title == "Nice Apartment"
    assert place.price == 250.5
    assert place.owner == owner
    assert isinstance(place.reviews, list)
    assert isinstance(place.amenities, list)

    #Try adding a review and attachment
    class DummyReview: pass
    class DummyAmenity: pass

    review = DummyReview()
    amenity = DummyAmenity()

    place.add_review(review)
    place.add_amenity(amenity)

    assert review in place.reviews
    assert amenity in place.amenities

    print(" Place test passed!")

if __name__ == "__main__":
    test_place()

