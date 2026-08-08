# 🎬 Cinema Seat Booking System

A simple **Object-Oriented Programming (OOP)** project written in **Python** that simulates a cinema hall seat booking system.

This project is part of the **Daily Python Exercises → 02. Intermediate → OOP** collection and focuses on practicing **classes, inheritance, object composition, and basic business logic**.

---

## 📌 Project Overview

The system allows you to:

* Create a cinema hall
* Add regular and VIP seats
* Book available seats
* Cancel booked seats
* Display seat status
* Calculate total revenue from booked seats

The main goal of this exercise is to strengthen **core OOP concepts** through a realistic scenario.

---

## 🧠 OOP Concepts Used

| Concept            | Implementation                                                |
| ------------------ | ------------------------------------------------------------- |
| **Class & Object** | `seat`, `VIP_seat`, `CinemaHall`                              |
| **Encapsulation**  | Seat data stored inside objects                               |
| **Inheritance**    | `VIP_seat(seat)` extends the base seat class                  |
| **Polymorphism**   | Revenue calculation handles regular and VIP seats differently |
| **Composition**    | `CinemaHall` contains multiple seat objects                   |

---

## 🗂️ Project Structure

```text
Cinema-Seat-Booking/
│
├── Cinema Seat Booking.py
└── README.md
```

---

## ⚙️ How It Works

### 1. Create a cinema hall

```python
hall = CinemaHall("Main Hall")
```

### 2. Create seats

```python
s1 = seat("A1", 100)
s2 = seat("A2", 100)
v1 = VIP_seat("V1", 200, "Popcorn")
```

### 3. Add seats to the hall

```python
hall.add_seat(s1)
hall.add_seat(s2)
hall.add_seat(v1)
```

### 4. Book seats

```python
hall.book_seat_id("A1")
hall.book_seat_id("V1")
```

### 5. Calculate revenue

```python
hall.calculate_total_revenue()
```

---

## 🪑 Seat Status Logic

| Status        | Meaning                             |
| ------------- | ----------------------------------- |
| `available`   | Seat is free                        |
| `booked`      | Seat has been reserved              |
| `in_progress` | Seat is temporarily being processed |

This provides a more realistic booking workflow than a simple `True/False` flag.

---

## 💎 VIP Seat Features

VIP seats inherit all functionality from the regular seat class and add:

* **Higher pricing** (`1.5 × basic price`)
* **Extra service support**

Example:

```python
VIP_seat("V1", 200, "Popcorn")
```

---

## ▶️ Example Output

```text
This seat is now booked successfully
This seat is now booked successfully
Total Revenue for Main Hall: 400.0
```

---

## 🚀 Run the Project

Make sure Python 3 is installed, then run:

```bash
python "Cinema Seat Booking.py"
```

---

## 🎯 Learning Goals

This exercise is designed to practice:

* Designing related classes
* Managing object state
* Using inheritance effectively
* Iterating through collections of objects
* Implementing simple real-world business rules

---

## 🔮 Possible Future Improvements

* Add **user input** for interactive booking
* Prevent duplicate seat IDs
* Save bookings to a **file or database**
* Add **different hall types**
* Implement **seat categories** (Standard / Premium / VIP)
* Create a **console menu interface**

---

## 🛠️ Technologies

* **Python 3**
* **Object-Oriented Programming**
* No external libraries required

---

## 📚 Part of

**Daily Python Exercises**

```text
02. Intermediate
└── OOP
    └── Cinema-Seat-Booking
```

---

## 👩‍💻 Author

**Romina Valinejad**

GitHub: **@rominavalinejad**

---

> 🎓 *A small project focused on learning how real-world booking systems can be modeled using Python classes and object-oriented design principles.*
