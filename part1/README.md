# 🏡 HBnB Evolution - UML Documentation

> 📊 **A Simplified Airbnb-Style Application – Designed & Documented by:**  
**Danah Alshehri, Leen Alsaleh, Shurooq Alabbadi**

![gift](https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif)

---

## 🧠 Project Overview

HBnB Evolution is a conceptual redesign of a simplified Airbnb-style application, focusing on comprehensive UML documentation and layered architecture design. This project aims to solidify the understanding of software design principles, architecture, and system interaction.

---

## 🎯 Objectives

- 📁 Create **Package Diagrams** for layered architecture.
- 🧱 Design **Class Diagrams** for business logic.
- 🔄 Model **Sequence Diagrams** for API call flows.
- 📜 Compile full **technical documentation** using UML standards.

---

## 💡 System Features

### 👤 User Management
- Users can register, update profiles, and be either regular users or administrators.
- Attributes: `first_name`, `last_name`, `email`, `password`, `is_admin`.

### 🏠 Place Management
- Users can list properties with: `title`, `description`, `price`, `latitude`, `longitude`.
- Each place is linked to an owner (user) and can include amenities.

### 📝 Review Management
- Reviews include `rating` and `comment`, linked to both user and place.

### 🛏️ Amenity Management
- Amenity attributes: `name`, `description`.
- Places can have multiple amenities.

---

## 🏗️ Architecture Overview

### 🔌 Presentation Layer (API & Services)
- Manages user interactions.
- Interfaces with business logic through the **Facade Pattern**.

### 🧠 Business Logic Layer (Models)
- Contains the application's core logic and rules.
- Entities: `User`, `Place`, `Review`, `Amenity`.

### 🗃️ Persistence Layer
- Handles data storage and retrieval.
- Communicates with business logic through repositories.

---

## 🔧 Technologies & Tools

- 🧩 **UML Tools:** draw.io, Mermaid.js
- 📝 **Documentation:** Markdown
- ⚙️ **Version Control:** Git + GitHub

---

## 🧬 Deliverables

1. ✅ **High-Level Package Diagram**
2. ✅ **Class Diagram for Business Logic**
3. ✅ **Sequence Diagrams for 4 API calls**
4. ✅ **Compiled Documentation with Explanatory Notes**

---

## 🚀 Why This Matters

Understanding architecture and modeling is key to building scalable and maintainable systems. This documentation serves as a blueprint for future development phases and ensures alignment with software engineering best practices.

---

## 💖 Meet the Team

| 👩‍💻 Name              | 💼 Role           |
|----------------------|------------------|
| Danah Alshehri       | Developer & QA   |
| Leen Alsaleh         | Documentation Lead |
| Shurooq Alabbadi     | UML Designer     |

---

## 🎉 Special Touch

To celebrate completing this phase, here's a little animated gift for you!  
![gift](https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif)

---

## 📬 Manual QA Review

Once the documentation is complete, please request a **manual QA review** as part of the evaluation process.

---

## 📂 Repo Structure


holbertonschool-hbnb/
└── part1/
├── UML_Diagram/
│ ├── Package Diagram.png
│ ├── Class Diagram.png
│ ├── sequence_user_registration.png
│ └── ...
├── README.md
└── technical_documentation.pdf


---

### 📌 Notes

- All entities should include `id`, `created_at`, and `updated_at`.
- Use **UML notation** accurately and consistently.
- Follow **SOLID principles** for class design.

---

🔚 **Good luck on the rest of the project – keep designing like pros!**

تحرير
