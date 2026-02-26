# CarConnect – Vehicle Reservation and Management System

CarConnect is a database-driven vehicle reservation system developed using **Python** and **SQL Server**. The system allows customers to browse available vehicles, make reservations, and manage bookings, while administrators can manage vehicle records and monitor reservation activities.

This project is designed using a **layered architecture** to ensure modularity, scalability, and maintainability.

## Features

- Admin and Customer Authentication  
- Vehicle Management (Add, Update, Delete, View)  
- Real-Time Vehicle Reservation  
- Reservation Conflict Handling  
- Reservation History and Reports  
- Exception Handling and Input Validation  
- Unit Testing for Core Functionalities

## Tech Stack

- **Programming Language:** Python  
- **Database:** SQL Server  
- **Concepts:** OOP, CRUD Operations, SQL Joins, Window Functions  
- **Testing:** unittest
- 
## Project Structure
carconnect/
│
├── entity/ # Data models (Customer, Vehicle, Reservation, Admin)
├── dao/ # Database operations
├── service/ # Business logic
├── util/ # Database connection utilities
├── exception/ # Custom exceptions
└── main/ # Entry point of the application


## Database Tables

- Customer  
- Vehicle  
- Reservation  
- Admin  


## How to Run the Project

1. Create the **CARCONNECT** database in SQL Server.
2. Create required tables (Customer, Vehicle, Reservation, Admin).
3. Update database connection settings in the `util` module.
4. Run the main file:


5. Use the menu-driven console to test features.

---

## Key Functional Modules

- User Authentication System  
- Vehicle CRUD Management  
- Reservation System with Validation  
- Reporting using SQL Queries  

---

## Learning Outcomes

- Implemented layered architecture using Python  
- Strengthened SQL query writing and optimization  
- Developed real-time booking validation logic  
- Practiced exception handling and unit testing

---

## Future Enhancements

- Email/SMS Notifications  
- Web-based UI using MERN or Flask  
- Dashboard for analytics and visualization

---

## Author

**Deepana**

---

## If you like this project

Give it a on GitHub and feel free to fork or contribute!

