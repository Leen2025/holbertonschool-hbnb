import uuid
from datetime import datetime

class Amenity:
    def __init__(self, name):
        """
        Initialize a new Amenity instance.

        Args:
            name (str): The name of the amenity (e.g., "Wi-Fi", "Parking").
                        This is a required attribute and must be max 50 characters.
        """
        self.id = str(uuid.uuid4())  # Unique identifier for the amenity
        self.name = name  # Amenity name
        self.created_at = datetime.now()  # Timestamp when created
        self.updated_at = datetime.now()  # Timestamp when last updated

    def save(self):
        """
        Update the updated_at timestamp whenever the amenity is modified.
        """
        self.updated_at = datetime.now()

    def update(self, data):
        """
        Update the attributes of the amenity.

        Args:
            data (dict): Dictionary containing keys and values to update.
        """
        if 'name' in data:
            self.name = data['name']
        self.save()  # Update timestamp after modification

# Example of usage
if __name__ == "__main__":
    amenity = Amenity("Wi-Fi")
    print(f"Amenity created with ID: {amenity.id} and name: {amenity.name}")
