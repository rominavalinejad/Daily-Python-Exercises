# 🎬 Cinema Seat Booking System

A simple **Object-Oriented Programming (OOP)** project written in **Python** that simulates a cinema seat reservation system.

The project models a real-world cinema booking workflow using multiple related classes such as **seats, cinema halls, movies, screenings, bookings, and customers**.

This project is part of the **Daily Python Exercises → 02. Intermediate → OOP** collection and focuses on practicing **classes, inheritance, composition, object relationships, state management, and basic business logic**.

---

## 📌 Project Overview

The system currently supports:

* Creating a cinema hall
* Creating regular and VIP seats
* Automatically generating cinema seats
* Managing seat availability
* Booking available seats
* Creating customer records
* Generating reservation codes
* Validating Iranian mobile phone numbers
* Creating movie screenings
* Connecting bookings to customers, screenings, and seats
* Displaying all seat statuses
* Calculating total cinema revenue
* Interactive command-line booking

The main goal of this project is to practice designing a small real-world system using **Object-Oriented Programming principles**.

---

## 🧠 OOP Concepts Used

| Concept                  | Implementation                                                                                            |
| ------------------------ | --------------------------------------------------------------------------------------------------------- |
| **Class & Object**       | `Seat`, `VIP_seat`, `CinemaHall`, `Movie`, `Screening`, `Booking`, `Customer`                             |
| **Encapsulation**        | Seat, customer, movie, screening, and booking data are stored inside objects                              |
| **Inheritance**          | `VIP_seat` inherits from `Seat`                                                                           |
| **Composition**          | `CinemaHall` contains multiple `Seat` objects                                                             |
| **Object Relationships** | `Screening` connects a movie with a cinema hall, while `Booking` connects a customer, screening, and seat |
| **State Management**     | Seats use `available`, `booked`, and `in_progress` states                                                 |
| **Polymorphism**         | Revenue calculation handles regular and VIP seats based on their available attributes                     |

---

## 🗂️ Project Structure

```text
Cinema-Seat-Booking/
│
├── Cinema Seat Booking.py
└── README.md
```

The current implementation is contained in a single Python file.

---

# 🏗️ Main Classes

## 🪑 `Seat`

The base class representing a regular cinema seat.

```python
Seat(seat_id, basic_price)
```

Each seat contains:

* `seat_id`
* `basic_price`
* `status`

A newly created seat starts with:

```text
available
```

### Seat Booking

The `Book()` method changes an available seat to:

```text
booked
```

It also handles seats that are already booked or currently in progress.

### Seat Cancellation

The `Cancel()` method changes a booked seat back to:

```text
available
```

---

## 💎 `VIP_seat`

`VIP_seat` inherits from the regular `Seat` class.

```python
class VIP_seat(Seat):
```

VIP seats add:

* A higher ticket price
* An extra service

The VIP price is calculated as:

```text
VIP price = basic price × 1.5
```

Example:

```python
VIP_seat(
    "VIP-A1",
    200,
    "Popcorn + Drink"
)
```

This creates a VIP seat with:

```text
Basic Price: 200
VIP Price: 300
Extra Service: Popcorn + Drink
```

---

## 🏛️ `CinemaHall`

The `CinemaHall` class represents a cinema hall and manages its seats.

```python
hall = CinemaHall("Main Hall")
```

The hall stores its seats inside:

```python
self.seat_list
```

### Adding Seats

Seats can be added using:

```python
hall.add_seat(new_seat)
```

### Displaying Seats

The current seat layout and status can be displayed using:

```python
hall.show_seat()
```

Example:

```text
--- Seats in Main Hall ---

A1         | available
A2         | booked
A3         | available
...
VIP-A1     | available
```

### Revenue Calculation

The hall can calculate the total revenue from all booked seats:

```python
hall.calculate_total_revenue()
```

Regular seats use their `basic_price`, while VIP seats use their `VIP_price`.

---

# 🎥 `Movie`

The `Movie` class stores information about a movie.

```python
Movie(title, duration, genre)
```

Each movie contains:

* `title`
* `duration`
* `genre`

Example:

```python
my_movie = Movie(
    "Inception",
    148,
    "Sci-Fi"
)
```

Another movie can be created as:

```python
my_movie_2 = Movie(
    "Interstellar",
    169,
    "Sci-Fi"
)
```

---

# 🕐 `Screening`

The `Screening` class represents a specific showing of a movie in a cinema hall.

```python
Screening(movie, hall, start_time)
```

A screening connects:

```text
Movie
   ↓
Screening
   ↓
Cinema Hall
```

For example:

```python
my_screening = Screening(
    my_movie,
    hall,
    "18:00"
)
```

The screening also maintains its own list of bookings:

```python
self.bookings = []
```

---

## 🎟️ Booking a Seat Through a Screening

Seat reservations are handled by:

```python
screening.book_seat(customer, seat_id)
```

The method:

1. Searches for the requested seat.
2. Checks whether the seat exists.
3. Checks whether the seat is available.
4. Books the seat.
5. Creates a `Booking` object.
6. Stores the booking inside the screening.
7. Returns the created booking.

Example:

```python
booking = my_screening.book_seat(
    customer,
    "A5"
)
```

If the seat is not available, the booking will not be created.

---

# 🎫 `Booking`

The `Booking` class represents a reservation made by a customer.

```python
Booking(customer, screening, seat)
```

Each booking connects three important objects:

```text
Customer
   │
   ├── Booking
   │
Screening
   │
   └── Seat
```

A booking currently stores:

* `customer`
* `screening`
* `seat`

This creates a relationship between the customer, selected screening, and reserved seat.

---

# 👤 `Customer`

The `Customer` class stores customer information.

```python
Customer(name, phone)
```

Each customer has:

* `name`
* `phone`
* `reservation_code`

The reservation code is automatically generated when the customer object is created.

Example:

```text
RES5832
```

The code is generated using a random four-digit number:

```python
RES + random number
```

---

# 📱 Customer Input & Phone Validation

The project includes an interactive function for creating customers:

```python
create_customer()
```

The system asks for:

```text
Enter customer name:
Enter phone number:
```

The phone number must:

* Contain only digits
* Have exactly 11 digits
* Start with `09`

Example of a valid number:

```text
09123456789
```

If the number is invalid, the system asks the user to enter it again.

---

# 🪑 Seat Layout

The cinema hall is automatically populated with **140 seats**.

## Regular Seats

There are **100 regular seats**.

They are organized into rows:

```text
A → J
```

Each row contains:

```text
1 → 10
```

The generated seat IDs look like:

```text
A1
A2
A3
...
J10
```

Each regular seat has a basic price of:

```text
100
```

---

## VIP Seats

There are **40 VIP seats**.

They are organized into:

```text
VIP-A1 → VIP-A10
VIP-B1 → VIP-B10
VIP-C1 → VIP-C10
VIP-D1 → VIP-D10
```

Each VIP seat has:

```text
Basic Price: 200
VIP Price: 300
Extra Service: Popcorn + Drink
```

---

# 🎬 Current Movies & Screenings

The example application currently creates two movies:

| Movie        | Duration | Genre  |
| ------------ | -------: | ------ |
| Inception    |  148 min | Sci-Fi |
| Interstellar |  169 min | Sci-Fi |

Two screenings are also created:

| Movie        | Start Time |
| ------------ | ---------- |
| Inception    | 18:00      |
| Interstellar | 20:30      |

---

# 🖥️ Command-Line Interface

The application provides a simple interactive menu:

```text
=== Cinema Booking System ===

1. Show seats
2. Book a seat
3. Show revenue
4. Exit
```

## 1. Show Seats

Displays all seats in the cinema hall and their current status.

```text
A1         | available
A2         | booked
VIP-A1     | available
```

---

## 2. Book a Seat

The system asks for customer information and then requests a seat ID.

Example:

```text
Enter customer name: Ali
Enter phone number: 09123456789
Enter seat ID: A5
```

If the booking succeeds:

```text
This seat is now booked successfully

Seat A5 booked for Ali
Reservation Code: RES5832
```

---

## 3. Show Revenue

Displays the total revenue generated from currently booked seats.

Example:

```text
Total Revenue for Main Hall: 400
```

---

## 4. Exit

Closes the application.

```text
Goodbye!
```

---

# 🔄 Seat Status Logic

Each seat can have one of three statuses:

| Status        | Meaning                                 |
| ------------- | --------------------------------------- |
| `available`   | The seat is currently free              |
| `booked`      | The seat has been reserved              |
| `in_progress` | The seat is temporarily being processed |

The basic booking flow is:

```text
available
    ↓
  booked
```

A booked seat can also be cancelled:

```text
booked
    ↓
available
```

The `in_progress` state is already supported by the `Seat` class and can be used later for a more advanced temporary reservation workflow.

---

# 🔗 Object Relationships

The main relationships in the current system can be represented as:

```text
                 ┌─────────────┐
                 │    Movie    │
                 └──────┬──────┘
                        │
                        ▼
                 ┌─────────────┐
                 │  Screening  │
                 └──────┬──────┘
                        │
                ┌───────┴────────┐
                ▼                ▼
        ┌─────────────┐   ┌─────────────┐
        │ CinemaHall  │   │   Booking   │
        └──────┬──────┘   └──────┬──────┘
               │                 │
               ▼          ┌──────┴──────┐
        ┌─────────────┐    │             │
        │    Seat     │    ▼             ▼
        └──────┬──────┘ Customer       Seat
               │
          ┌────┴─────┐
          ▼          ▼
       Regular      VIP
        Seat        Seat
```

This structure demonstrates how multiple objects can work together to model a real-world booking system.

---

# ▶️ Run the Project

Make sure **Python 3** is installed.

Then run:

```bash
python "Cinema Seat Booking.py"
```

No external packages are required.

The project only uses Python's built-in `random` module.

---

# 🎯 Learning Goals

This exercise is designed to practice:

* Creating classes and objects
* Using inheritance
* Designing relationships between objects
* Managing object state
* Working with lists of objects
* Implementing basic business logic
* Creating reusable methods
* Handling user input
* Validating user input
* Generating unique-looking reservation codes
* Connecting multiple domain objects together
* Building a simple CLI application

---

# 🔮 Possible Future Improvements

The current project provides the basic foundation of a cinema booking system. Possible future improvements include:

* Add a proper seat cancellation option to the CLI
* Add booking cancellation through a reservation code
* Prevent duplicate reservation codes
* Use `datetime` for real screening dates and times
* Support multiple cinema halls
* Support multiple screenings independently
* Prevent the same seat from being booked across conflicting screenings
* Add a payment system
* Add customer booking history
* Store bookings in a file or database
* Add an admin interface
* Improve the `in_progress` temporary reservation workflow
* Separate classes into multiple Python modules
* Add unit tests
* Add a graphical or web-based interface

---

# 🛠️ Technologies

* **Python 3**
* **Object-Oriented Programming (OOP)**
* **Python Standard Library**
* No external dependencies

---

# 📚 Part of

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

> 🎓 *A learning project focused on modeling a real-world cinema reservation system using Python and Object-Oriented Programming principles.*
