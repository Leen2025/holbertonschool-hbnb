# 🏡 HBnB Project: Technical Documentation

![HBnB Cover](https://github.com/user-attachments/assets/5efaf133-f174-42b6-bdd7-986f40ef9b17)

---

## 📌 Introduction

Welcome to the technical backbone of **HBnB Evolution** — a project inspired by **Airbnb** 🛏️. This system allows users to:

- List accommodations for rent
- Submit and read reviews
- Search for the perfect stay

This document outlines the system’s **architecture**, **design**, and **UML diagrams**, offering a clear, layered reference to guide development and maintenance.

---
# PART1 
## 🍳 What’s Cooking in Part 1?

### ✏️ Sketching with UML

We start by designing our application's skeleton using **UML (Unified Modeling Language)** — defining the relationship between major components and setting the foundation for development.

---

## 🏗️ High-Level Architecture

### 📦 High-Level Package Diagram
<p align="center">
  <img src="https://github.com/user-attachments/assets/85ee871a-6fe6-44c7-a079-fb09cbd53bbc" alt="Package Diagram" width="700" />
</p>

### 🧱 Description

Our architecture uses a **multi-layered approach** to promote separation of concerns, better maintainability, and modularity.

---

## 🧬 The Three Layers of Our API

| Layer               | Responsibilities |
|---------------------|------------------|
| **🔹 Presentation Layer (API)** | - Handles incoming HTTP requests<br>- Validates input<br>- Sends tasks to Business Logic Layer |
| **🔸 Business Logic Layer** | - Contains the core logic and domain models<br>- Handles authentication, validation, business rules |
| **🔻 Persistence Layer (Database)** | - Manages data access (initially file-based)<br>- Saves and retrieves entities |

> 🧰 **Design Pattern Used**: `Facade Pattern`  
> Simplifies interaction between API and data by wrapping complex operations in unified services.

---

## ⚙️ Business Logic Layer

### 📐 Class Diagram

<p align="center">
  <img src="https://github.com/user-attachments/assets/7383e1d2-696d-45de-ac37-d63ea899a019" alt="Class Diagram" width="700" />
</p>

### 🧩 Description

This section breaks down the structure and relationships within the business logic core.

## ⚙️Class Attributes And Opreation  :
## User👥
### Attributes :
` Id `,`frist name` ,`last name ` , `email ` ,  `password ` , ` created_at ` ,  ` updated_at ` , ` is_admin  `  
### Opration :
` register  `,  `update_profile` ,  `delete_user` ,  `authenticate `

 ## Place🏘️
 ### Attributes :
 ` Id `, `title ` ,`description ` , ` price ` ,  ` latitude ` ,` longitude` , ` created_at ` ,  ` updated_at `
 ### Opration :
` create_place  `,  `update_place` ,  `delete_place` ,  `list_amenities `

## Review📝
### Attributes :
` Id `, `rating` ,`commint ` , ` created_at ` ,  ` updated_at `  
### Opration :
`create_review  `,  `update_review` ,  `delete_review` ,  `list_review_by_place `

## Amenity✨
### Attributes :
` Id `, ` name` ,`description ` ,` created_at ` ,  ` updated_at ` 
### Opration :
`create_amenity `,  `update_amenity` ,  `delete_amenity` ,  `list_amenities `

---

## 🔑  **Key Classes**
- **User**  
  Represents system users with credentials and profile data.  
  Methods:  
  - `register()`  
  - `update_profile()`  
  - `delete_user()`  
  - `authenticate()`

- **Place**  
  Represents a listed property/place with location, description, and pricing.  
  Methods:  
  - `create_place()`  
  - `update_place()`  
  - `delete_place()`  
  - `list_amenities()`

- **Review**  
  Represents user feedback about places.  
  Methods:  
  - `create_review()`  
  - `update_review()`  
  - `delete_review()`  
  - `list_reviews_by_place()`

- **Amenity**  
  Represents services/facilities that can be associated with places.  
  Methods:  
  - `create_amenity()`  
  - `update_amenity()`  
  - `delete_amenity()`  
  - `list_amenities()`

---

🔗 **Relationships**
 `User ` → ` Place `: 1:* (User owns multiple Places)

 `User ` →  `Review `: 1:* (User writes multiple Reviews)

 `Place ` → ` Review ` : 1:* (Place has multiple Reviews)

---

💡 **Design Highlights**
- **Encapsulation**: Each class focuses on specific responsibilities.
- **Reusability**: Common models like `User` and `Amenity` are reused.
- **Scalability**: Flexible structure for future features.
- **Clarity**: Clear separation between data and behavior.
---

## 🗂️ The Data Model: Key Entities

### 🏘️ Places

Accommodations listed in the system, described by:

- title, description, latitude ,longitude 
- Owner, price 
- Amenities & user reviews

### 👥 Users

Individuals using the platform as hosts or reviewers, defined by:

- Email (unique), password
- First name & last name

### 📝 Reviews

Feedback and ratings from users:

- Rating (1–5 stars)
- Comment & submission date

### ✨ Amenities

Selectable features (e.g., Wi-Fi, pool), with an option to customize.

---

## 🔄 API Interaction Flow

### 📊 Sequence Diagram:

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/4b45cad1-de1e-4bae-bf7a-d80bb3f6ab70" alt="Sequence1" width="300"></td>
    <td><img src="https://github.com/user-attachments/assets/3221183b-8869-48e8-92ac-5a478a38181a" alt="Sequence2" width="300"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/81830b71-eeb8-4a56-921b-80eacf5f66e0" alt="Sequence3" width="300"></td>
    <td><img src="https://github.com/user-attachments/assets/af2fe1c3-004c-4f59-9478-4ad238918b94" alt="Sequence4" width="300"></td>
  </tr>
</table>


### 🧭 EX Steps for registration

- User ->> API: registration(username, email, password)
- API ->> BusinessLogic: validateUser()
-   BusinessLogic ->> BusinessLogic: validated
-   BusinessLogic ->> BusinessLogic: createUser()
-   BusinessLogic ->> Database: saveUser()
-   Database -->> BusinessLogic: success
-   BusinessLogic -->> API: User Created
-   API -->> User: 201 Created

### 📝 Description

Illustrates how user data travels from the User to the Persistence layer, highlighting key validations and success responses.

- Status Code: **`201 Created`**
- Clean, modular communication between components

---

## 🧾 Essential Entity Attributes

| Attribute | Description |
|-----------|-------------|
| `UUID4`   | Unique, non-colliding identifier for every entity |
| `created_at` | Timestamp marking creation time |
| `updated_at` | Timestamp for the last update |

### 🧠 Why They Matter?

- **🔐 Uniqueness:** Ensures global distinction of records
- **🧮 Auditability:** Tracks object history for transparency and debugging

---

## ✅ Conclusion

This technical documentation acts as a **blueprint** for the HBnB project:

- Promotes **clarity**, **consistency**, and **alignment** with software engineering best practices
- Brings together architecture, design, and rationale for collaborative success

---
---

## 📂 View Full Diagrams

If you'd like to explore all the diagrams and illustrations used in this project, you can visit the diagrams folder here:

[Go to UML_Diagram folder](https://github.com/Leen2025/holbertonschool-hbnb/tree/main/part1/UML_Diagram)

---

## 📁 GitHub Repository

🔗 **Repo:** [holbertonschool-hbnb](https://github.com/Leen2025/holbertonschool-hbnb)  
📂 **Directory:** `/part1`

---
# PART 2 


# HBnB - Part 2: API Implementation and Business Logic

## 🧠 Overview

This part of the HBnB project focuses on implementing the **Business Logic** and **API Endpoints** using Python and Flask. It builds upon the foundational elements of the application to provide RESTful services that manage core models such as `User`, `Place`, `State`, `City`, and more.

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

hbnb/
├── api/
│ └── v1/
│ ├── app.py
│ └── views/
│ ├── index.py
│ ├── places.py
│ ├── users.py
│ ├── states.py
│ ├── cities.py
│ └── amenities.py
├── models/
│ ├── place.py
│ ├── user.py
│ ├── state.py
│ ├── city.py
│ └── amenity.py



---

## ✅ Testing Tips

- Always set `Content-Type: application/json` when using `POST` or `PUT`.
- Use `curl -i` to show response headers and status codes.
- Test both successful and error scenarios.
- Make sure each endpoint returns valid JSON.

---



## 📌 Notes

- All endpoints follow RESTful principles.
- Input and output data is strictly JSON.
- Proper testing and validation are essential for backend quality.





## 👩‍💻 Contributing Team

| Name                   | GitHub Handle |
|------------------------|----------------|
| Leen Mohammed Alsaleh | [@Leen2025](https://github.com/Leen2025) |
| Danah Alshehri         | [@d-alshehri](https://github.com/d-alshehri) |
| Shurooq Alabbadi       | [@ShAlabbadi](https://github.com/ShAlabbadi) |

---

🧠 **"Thank you for taking the time to explore our project. We’re deeply grateful for the opportunity to build, learn, and grow together. Here’s to innovation, teamwork, and the journey ahead!"** 🌟
![Celebration](https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif)

