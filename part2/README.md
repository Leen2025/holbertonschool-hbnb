---
# PART 2 


# HBnB - Part 2: API Implementation and Business Logic

## 🧠 Overview

This part of the project focuses on implementing the core functionality of the application by establishing its structure, defining the business logic through class development, and creating the necessary API endpoints. The objective is to bring the documented architecture to life by enabling the creation and management of key resources such as users, places, reviews, and amenities. All components are designed in accordance with best practices for API development, ensuring scalability, modularity, and maintainability throughout the application.

---

## 📝 Tasks Breakdown

### 🔹 Task 0: Base API Setup

- Set up Flask application structure.
- Created basic `/status` route to return a simple JSON response.
- Verified app runs using:

```bash
python3 -m api.v1.app

Test with:
curl http://127.0.0.1:5000/api/v1/status

````
---

### 🔹 Task 1: Implement Place CRUD Endpoints

- Developed routes for `/places` and `/places/<place_id>`.
- Implemented Create, Read, Update, and Delete functionality.
- JSON input validation added.

Example:

curl -X POST http://127.0.0.1:5000/api/v1/places/
-H "Content-Type: application/json"
-d '{"name": "My place", "city_id": "xyz", "user_id": "abc"}'


---

### 🔹 Task 2: Implement City and State Endpoints

- Created endpoints:
  - `/states`
  - `/states/<state_id>`
  - `/states/<state_id>/cities`
  - `/cities/<city_id>`
- Enabled retrieving, creating, and deleting cities related to a state.

---

### 🔹 Task 3: Implement User Endpoints

- Built endpoints for:
  - `/users`
  - `/users/<user_id>`
- CRUD operations:
  - Create user
  - Update user
  - Delete user
- Validated required fields like `email` and `password`.
- 
![Image](https://github.com/user-attachments/assets/311797f0-fd06-4949-be64-df049aebddcb)
---

### 🔹 Task 4: Implement Amenity Endpoints

- Developed full set of routes for `/amenities` and `/amenities/<amenity_id>`.
- Supports `POST`, `GET`, `PUT`, and `DELETE` methods.
- Added input validation and handled errors appropriately.
![Image](https://github.com/user-attachments/assets/2671ce31-b716-4e1c-aa64-ea8d35d000aa)
---

### 🔹 Task 5: Handle Missing Routes and Errors

- Implemented proper error handling:
  - `404 Not Found` for invalid endpoints
  - `400 Bad Request` for malformed JSON
- Used Flask error handlers to ensure all error responses are JSON formatted.

---

### 🔹 Task 6: Testing and Validation

- Manually tested all endpoints using `curl`.
- Validated:
  - Successful creation and update of objects
  - Error responses for invalid input
  - Required fields missing
  - Wrong data types or non-existent IDs
- Ensured appropriate HTTP response codes are returned.
- 
![Image](https://github.com/user-attachments/assets/9f10c847-ccf9-4ac2-bedc-0bceda0e684d)


Examples:

**Create a User:**

curl -X POST http://127.0.0.1:5000/api/v1/users/
-H "Content-Type: application/json"
-d '{"email": "user@example.com", "password": "1234"}'


**Update a User:**



curl -X PUT http://127.0.0.1:5000/api/v1/users/<user_id>
-H "Content-Type: application/json"
-d '{"first_name": "UpdatedName"}


**Delete a User:**

curl -X DELETE http://127.0.0.1:5000/api/v1/users/<user_id>





---

## 📂 Project Structure

 ```text
    hbnb/
    ├── app/
    │   ├── __init__.py
    │   ├── api/
    │   │   ├── __init__.py
    │   │   ├── v1/
    │   │       ├── __init__.py
    │   │       ├── users.py
    │   │       ├── places.py
    │   │       ├── reviews.py
    │   │       ├── amenities.py
    │   ├── models/
    │   │   ├── __init__.py
    │   │   ├── user.py
    │   │   ├── place.py
    │   │   ├── review.py
    │   │   ├── amenity.py
    │   ├── services/
    │   │   ├── __init__.py
    │   │   ├── facade.py
    │   ├── persistence/
    │       ├── __init__.py
    │       ├── repository.py
    ├── run.py
    ├── config.py
    ├── requirements.txt
    ├── README.md
    ```
 ```


---

## ✅ Testing Tips

- Always set `Content-Type: application/json` when using `POST` or `PUT`.
- Use `curl -i` to show response headers and status codes.
- Test both successful and error scenarios.
- Make sure each endpoint returns valid JSON.

---
