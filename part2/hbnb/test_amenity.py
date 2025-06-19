from app.models.amenity import Amenity

def test_amenity():
    amenity = Amenity("Wi-Fi")
    assert amenity.name == "Wi-Fi"
    print("Amenity test passed!")

if __name__ == "__main__":
    test_amenity()
