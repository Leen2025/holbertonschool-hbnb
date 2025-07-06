# 🏠 HBnB - Home & Beyond Booking

---
![Home Sweet Home](https://media.giphy.com/media/l4FGuhL4U2WyjdkaY/giphy.gif)



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

# 🏠 HBnB - Home & Beyond Booking

---

![HBnB Banner](https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80)

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


# 📎 View the full database diagram here: [ER Diagram](./er_diagram.md)

## 🙌 Thank You!
If you need any help or want to contribute, feel free to reach out. Let’s build great things together! 🚀✨
