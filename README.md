# HBnB Project: Technical Documentation

![Image](https://github.com/user-attachments/assets/5efaf133-f174-42b6-bdd7-986f40ef9b17)

## Introduction
HBnB Evolution aims to replicate the functionality of AirBnB, allowing users to list places for rent, write reviews, and search for accommodations. This first part , This technical document outlines the architectural and design structure of the **HBnB** project. It compiles all the design artifacts package diagram, class diagram, and sequence diagrams into one cohesive reference. The document provides a comprehensive overview of the system's layered architecture, core components, and interactions to guide implementation and maintenance.

---
## What’s Cooking in Part 1? 

### Sketching with UML:
Start by sketching out the application's backbone using UML (Unified Modeling Language) to create a blueprint for how our classes and components will interact. This step is crucial for visualizing the structure and relationships between different parts of our application.


## High-Level Architecture
 
### Diagram: High-Level Package Diagram

![Image](https://github.com/user-attachments/assets/8e181c6c-bbc4-41b1-9c4a-a0408992ff9d)


### Description

The high-level architecture follows a multi-layered design that separates concerns for better modularity and maintainability.

## The Three Layers of Our API 

- **Presentation Layer (API):**  
  Handles incoming HTTP requests, validates input, and delegates tasks to the Business Logic Layer.
Handles incoming requests and outgoing responses via the API. It acts as the interface between the client and the application's core logic.

- **Business Logic Layer:**  
  Contains the core application logic and domain models. Acts as a mediator between the API and Persistence layers.
Core processing and decision-making component of the application. Here, rules such as user authentication, data validation, and business workflows are implemented.
- **Persistence Layer (Database):**  
  Manages direct access to the data sources. Encapsulates all the logic for saving and retrieving data.
Initially file-based, storing and retrieving data for the application. This layer interacts directly with the storage mechanism (e.g., files) to manage the application's data.
### Design Pattern Used: Facade Pattern

The **Facade** in the Business Logic Layer simplifies interactions between the API and the underlying subsystems (e.g., repositories).

---

## Business Logic Layer

### Diagram: Detailed Class Diagram

 ![Image](https://github.com/user-attachments/assets/7383e1d2-696d-45de-ac37-d63ea899a019)

### Description

This diagram provides a deep dive into the core components and relationships within the Business Logic Layer.

#### Key Classes

- `User`: Represents a user entity with properties like `id`, `email`, `password`.
- `UserService`: Provides business operations such as registration, validation, and retrieval of users.
- `Repositories`: Interface for data access (e.g., `UserRepository`) to abstract database interactions.

#### Relationships

- `UserService` depends on `UserRepository` for persistence operations.
- `User` is a model used across various services and layers.

#### Design Decisions

- Services are **stateless** and **testable**.
- Repositories are injected as dependencies for **loose coupling**.

---
## The Data Model: Key Entities 📝

### Places:
Places are the core entities of our application, representing accommodations available for rent. Each place includes attributes such as:
- Name, description
- Address, city, latitude, longitude
- Host (owner)
- Number of rooms, bathrooms
- Price per night, max guests
- Amenities (features like Wi-Fi, pools)
- Reviews (user feedback and ratings)

### Users:
Users are individuals interacting with the application, categorized as hosts (owners of places) or reviewers (users leaving reviews). Key attributes include:
- Email (unique identifier)
- Password
- First name, last name

### Reviews:
User-generated feedback and ratings for places. Each review contains:
- Rating (e.g., 1-5 stars)
- Comment
- Date of submission

### Amenities:
Features available in places, such as Wi-Fi, pools, etc. Users can select from a predefined catalog or add new amenities as needed.

## API Interaction Flow

### Diagram: Sequence Diagram for User Registration

![Image](https://github.com/user-attachments/assets/4b45cad1-de1e-4bae-bf7a-d80bb3f6ab70)

### Steps


- User ->> API: registration(username, email, password)
- API ->> BusinessLogic: validateUser()
-   BusinessLogic ->> BusinessLogic: validated
-   BusinessLogic ->> BusinessLogic: createUser()
-   BusinessLogic ->> Repository: saveUser()
-   Repository -->> BusinessLogic: success
-   BusinessLogic -->> API: User Created
-   API -->> User: 201 Created


###  Description

This interaction illustrates the flow of a **registration API call** from the front-end to database insertion.

- `201 Created`: HTTP status code indicating successful resource creation.
- Emphasis is on validation and separation of responsibilities across layers.

###  Design Rationale

- The sequence ensures **modular validation**, **safe persistence**, and **clear response communication**.
- Aligns with **RESTful API design principles**.

---
## Essential Attributes for Every Entity 

- **Unique ID (UUID4):** Globally unique identifier for each entity, ensuring no overlap or ambiguity in data identification.
  
- **Creation Date (`created_at`):** Timestamp indicating when an object was created, essential for auditing and data lifecycle management.
  
- **Update Date (`updated_at`):** Timestamp recording the last modification made to an object, aiding in tracking data changes and maintaining accuracy over time.

## Why These Attributes Matter? 

- **Uniqueness:** UUID4 ensures each entity is distinct, crucial for scalable and reliable data management.
  
- **Traceability:** `created_at` and `updated_at` timestamps provide a clear audit trail of entity lifecycle, facilitating debugging, auditing, and user interaction analysis.

##  Conclusion

This document serves as the **blueprint for implementing the HBnB project**. It ensures consistency in architectural decisions and provides a clear reference for team members. All diagrams and descriptions are aligned with **best practices** in software architecture and **object-oriented design**.

---

##  GitHub Repository

**Repository:** [holbertonschool-hbnb](https://github.com/Leen2025/holbertonschool-hbnb)  
**Directory:** `/part1`

---
## Contributing 
- **Leen Mohammed Alsaleh** - [@Leen2025](https://github.com/Leen2025)
- **Danah Alshehri** - [@d-alshehri](https://github.com/d-alshehri)
- **Shurooq alabbadi** - [@ShAlabbadi](https://github.com/ShAlabbadi)



