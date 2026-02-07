# TipsByJ – Salon Booking System (OOP Project)

## Overview
A console-based salon booking system developed in Python with Object-Oriented Programming (OOP) features for managing a salon's artists, services and client appointments.
The system has been designed in a structured and organized manner to allow a salon to easily access and manage its resources.

This project was developed as part of an OTHM Level 4 module to demonstrate my understanding of OOP concepts, good modular design and the basics of data persistence.

---

## Features
- Access to all available nail artists along with their working schedule
- View all available salon services (Manicure, Pedicure, Acrylic Set, Polygel Tips)
- Create appointments while avoiding double bookings
- Use of JSON for storing appointment data
- A simple and easy-to-use interactive console menu

---

## Object-Oriented Design
The system employs the fundamental principles of OOP:
- **Encapsulation**: The encapsulation principle states that you should group your data and behavior into classes.
- **Inheritance**: Service types inherit from a base `Service` class.
- **Polymorphism**: Each service type will have its own version of the `serviceDetails()` method where it can provide its own details about how to perform the service.
- **Abstraction**: The high-level booking logic is implemented in the `SalonManager` class.

---

## Project Structure
