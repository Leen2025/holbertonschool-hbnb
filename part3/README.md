
# 🏠 HBnB - Home & Beyond Booking

---
![Welcome Tech](https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif)

---

## 📖 Introduction

Welcome to **HBnB** — your modern, secure, and flexible home booking & management system. Whether you are a regular user or an administrator, **HBnB** lets you manage accounts, places, amenities, and reviews effortlessly with a clean architecture powered by modern tech.

**HBnB** combines:

- ⚡ **Flask RESTful API**  
- 🐍 **SQLAlchemy ORM** with SQLite (development)  
- 🔐 **JWT for authentication and authorization**  
- 🔒 **bcrypt for secure password hashing**  
- 📦 **Object-Oriented Programming & Layered Architecture**

---

## 🛠️ Features

| Feature                         | Description                                                                                  |
|--------------------------------|----------------------------------------------------------------------------------------------|
| 🎭 **Role-Based Access Control** | Regular users manage their own data. Admins can manage all resources with full privileges.   |
| 🧩 **Accurate Data Modeling**      | Core entities: User, Place, Review, Amenity with strong relationships & constraints.         |
| 🔑 **UUID Identifiers**             | Globally unique IDs for all entities ensuring robust data consistency.                       |
| 📚 **Repository Pattern**           | Generic SQLAlchemyRepository + specialized UserRepository for clean, maintainable code.      |
| 🔐 **Secure Password Management**   | Passwords hashed via bcrypt before storage with password verification.                       |
| 🚀 **Robust API Endpoints**          | JWT secured routes, admin-restricted endpoints, with precise permission checks.             |

---

## 🏗️ Technical Architecture

### 1. Application Environment

- Python 3.x  
- Flask & Extensions: SQLAlchemy, Bcrypt, JWT Extended  

### 2. Project Structure

```bash
app/
├── __init__.py           # App and DB setup
├── models/               # SQLAlchemy ORM models
│   ├── base_model.py     # BaseModel: UUID + timestamps
│   ├── user.py           # User entity mapping
│   ├── place.py          # Place entity mapping
│   ├── review.py         # Review entity mapping
│   └── amenity.py        # Amenity entity mapping
├── persistence/          # Repositories layer
│   ├── repository.py     # SQLAlchemyRepository & UserRepository
├── services/             # Business logic layer (Facade pattern)
└── api/                  # RESTful API endpoints with RBAC enforcement


```
### 3. Database Design Highlights

| Entity       | Key Attributes & Notes                                                         |
|--------------|--------------------------------------------------------------------------------|
| **User**       | UUID primary key, unique email, hashed password, boolean `is_admin`            |
| **Place**      | UUID primary key, title, description, price, latitude, longitude, linked to User (owner) |
| **Review**     | UUID primary key, text, rating (1-5), linked to User and Place                 |
| **Amenity**    | UUID primary key, unique name                                                  |
| **Place_Amenity** | Many-to-many association table linking Places and Amenities                  |

---

### ⚙️ Setup & Running Instructions

1. **Install Dependencies**

```bash
pip install -r requirements.txt
```
 ---

## ⚙️ Initialize Database

```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```
# Run the Application ▶️
```bash
flask run
```
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
🎨 Interactive Frontend UI

🔍 Advanced Search & Filtering of Places

🔔 Real-time Notifications & Updates

📈 User Activity Logging and Analytics Dashboard


# 📚 References
Flask Documentation

SQLAlchemy ORM Tutorial

Flask-Bcrypt

Flask-JWT-Extended

UUID Generation in Python
# Test 
<img src="https://github.com/user-attachments/assets/81840efe-722a-4229-900c-6207d960127c" alt="Image" width="500" />
<img src="https://github.com/user-attachments/assets/5645b4a0-f0a3-4c4d-a03a-6cf60efe0ddb" alt="Image" width="500" />
<img src="https://github.com/user-attachments/assets/da19c5e0-42e3-444e-8d2e-40e17d1628c7" alt="Image" width="500" />
<img src="https://github.com/user-attachments/assets/340620d6-c6ea-49bc-a030-50e70440b75a" alt="Image" width="500" />
<img src="https://github.com/user-attachments/assets/e936029f-5aa6-44bd-9c8d-454c118e516e" alt="Image" width="500" />
<img src="https://github.com/user-attachments/assets/3f4a7e0f-e4d1-4b12-be0b-cb8c88715236" alt="Image" width="500" />
<img src="https://github.com/user-attachments/assets/ea26350d-fe03-46fb-8ba6-000bd3e9710b" alt="Image" width="500" />
<img src="https://github.com/user-attachments/assets/bc283304-b33f-4cde-8702-65e8fc538f6d" alt="Image" width="500" />
<img src="https://github.com/user-attachments/assets/adaeaed7-d3d7-42d4-b3a6-ab80343f1878" alt="Image" width="500" />
<img src="https://github.com/user-attachments/assets/e22a6408-12c8-4cfa-bc19-0882e45c31e4" alt="Image" width="500" />

<img src="https://github.com/user-attachments/assets/1f284e88-c20d-45c5-abb5-fefec56d31eb" alt="Welcome Image" width="400" />
<br/>
<img src="https://github.com/user-attachments/assets/f837eeff-3c5f-440e-82f6-0a2a5c6a86b8" alt="Tech Image" width="400" />


# 📎 View the full database diagram here: [ER Diagram](./er_diagram.md)

## 🙌 Thank You!
If you need any help or want to contribute, feel free to reach out. Let’s build great things together! 🚀✨
![Abstract Tech](https://media.giphy.com/media/YTbZzCkRQCEJa/giphy.gif)
