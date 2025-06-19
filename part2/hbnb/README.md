# HBnB Project

## Project Structure

- `app/` contains the application's core code.
- `api/` contains the API interfaces.
- `models/` contains the data models.
- `services/` contains the Facade middleware.
- `persistence/` contains the In-Memory repository.
- `run.py` to run the application.
- `config.py` to configure the application.
- `requirements.txt` to specify the requirements.
- `README.md` to describe the project.

## Running the Project

1. Install the requirements:

pip install -r requirements.txt

markdown
Copy
Edit

2. Run the application:

python run.py

## Business Logic Layer

This part of the project implements the core classes that represent the main entities of the HBnB system.

### Implemented Classes:

- `User`: Represents an application user with name, email, and admin privileges.
- `Place`: Represents a listing owned by a user, with location, price, and amenities.
- `Review`: Represents a user’s review for a place, including a text and a rating from 1 to 5.
- `Amenity`: Represents additional features available in a place (Wi-Fi, Parking, etc.).

### Common Features:

- Each class inherits from `BaseModel`, which handles:
  - Unique UUID generation (`id`)
  - Timestamps: `created_at`, `updated_at`
  - `save()` method for tracking updates

### Relationships:

- A `User` can own multiple `Place`s.
- A `Place` can have multiple `Review`s and multiple `Amenity`s.
- A `Review` is tied to both a `Place` and a `User`.

Each class includes attribute validation to ensure data integrity.
 
