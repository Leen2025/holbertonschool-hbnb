
# 🏠 HBnB - Home & Beyond Booking

---

## 📖 Introduction

Welcome to **HBnB** — a modern home booking and management system designed to provide flexible and secure user experiences, supporting both regular users and administrators to manage accounts, places, amenities, and reviews seamlessly.

This project leverages cutting-edge technologies and a clean architectural design based on:

- **Flask RESTful API**  
- **SQLAlchemy ORM** with SQLite during development  
- **JWT for authentication and security**  
- **bcrypt for password hashing**  
- **Object-oriented programming and layered architecture**  

---

## 🛠️ Features

- **Role-Based Access Control (RBAC):**  
  - Regular users manage only their own accounts, places, and reviews.  
  - Admins have full privileges: create and modify any user, amenity, place, and review, bypassing ownership restrictions.

- **Accurate Data Modeling:**  
  - Core entities: User, Place, Review, Amenity.  
  - Clear relationships between entities (one-to-many, many-to-many) with strong constraints ensuring data integrity.

- **Flexible Database Design:**  
  - UUIDs for unique global identifiers.  
  - Unique constraints on critical fields (e.g., email, reviews per place per user).

- **Repository Pattern:**  
  - Unified CRUD operations using SQLAlchemyRepository.  
  - Specialized UserRepository for user-specific queries and logic.

- **Secure Password Management:**  
  - Password hashing with bcrypt before storing.  
  - Password verification implemented for authentication.

- **Robust API Endpoints:**  
  - Secure endpoints with JWT authentication.  
  - Admin-restricted endpoints with clear permission checks.

---

## 🏗️ Technical Architecture

### 1. Application Environment

- Python 3.x  
- Flask  
- Flask-SQLAlchemy  
- Flask-Bcrypt  
- Flask-JWT-Extended  

### 2. Project Structure

app/
├── init.py # App setup and DB initialization
├── models/ # SQLAlchemy models
│ ├── base_model.py # BaseModel with id and timestamps
│ ├── user.py
│ ├── place.py
│ ├── review.py
│ └── amenity.py
├── persistence/ # Repository layer with SQLAlchemyRepository & UserRepository
├── services/ # Business logic (Facade) layer
└── api/ # API endpoints with role-based access control



### 3. Database Design Highlights

- **User:** UUID primary key, unique email, hashed password, is_admin flag.  
- **Place:** UUID primary key, title, description, price, latitude, longitude, linked to a User (owner).  
- **Review:** UUID primary key, text, rating (1-5), linked to a User and a Place.  
- **Amenity:** UUID primary key, unique name.  
- **Place_Amenity:** Association table for many-to-many relationship between Place and Amenity.

---

## ⚙️ Setup & Running Instructions

1. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
 # Initialize Database
flask shell
>>> from app import db
>>> db.create_all()
# Run the Application
flask run
# 🔐 Role-Based Access Control (RBAC)
JWT tokens carry the is_admin claim to verify admin privileges.

Admin users: Full access, including user and amenity management, and override ownership restrictions.

Regular users: Limited to managing their own resources.

# 💡 Usage Examples
Admin creates new users and amenities.

Users create places and write reviews.

Fetch all places owned by a user.

Retrieve all reviews for a place.

Link amenities to places and query both ways.

# 🧪 Initial Data & Testing
SQL scripts provided to create tables and insert initial data, including an admin user with hashed password and several amenities.

CRUD operations tested via Postman or cURL to ensure data integrity and permission enforcement.

# 🚀 Future Enhancements
Interactive frontend UI.

Advanced place search and filtering.

Real-time notifications and updates.

User activity logging and analytics dashboard.

# 📚 References
Flask Documentation

SQLAlchemy ORM Tutorial

Flask-Bcrypt

Flask-JWT-Extended

UUID Generation in Python


# 📎 View the full database diagram here: [ER Diagram](./er_diagram.md)

## 🙌 Thank You!
If you need any help or want to contribute, feel free to reach out. Let’s build great things together! 🚀✨
