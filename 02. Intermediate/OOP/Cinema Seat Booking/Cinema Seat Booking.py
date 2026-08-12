'''
Cinema Seat Booking System (OOP core)
'''

import random


class Seat:
    def __init__(self, seat_id, basic_price):
        self.seat_id = seat_id
        self.basic_price = basic_price
        self.status = "available"

        # ''' The last method with two option: True/False'''
        # self.is_book = False
        # def book (self):
        #     if self.is_book == False:
        #         self.is_book = True
        #         print("This seat is now booked successfully")
        #     else:
        #         print("This seat is already booked")

        # def cancel (self):
        #     if self.is_book == True:
        #         self.is_book = False
        #         print("Booking cancel successfully")
        #     else:
        #         print("This seat is NOT booked yet")

    def Book(self):
        if self.status == "available":
            self.status = "booked"
            print ("This seat is now booked successfully")
        elif self.status == "in_progress":
            print("This seat is currently in progress by someone else. Try later!")
        elif self.status == "booked":
            print("This seat is already booked")

    def Cancel(self):
        if self.status == "booked":
            self.status = "available"
            print("Booking calnceled successfully")
        else:
            print("This seat is NOT booked yet!")

class VIP_seat(Seat):
    def __init__(self, seat_id, basic_price, extra_service="Welcome Drink"):
        super().__init__(seat_id, basic_price)
        self.VIP_price = basic_price * 1.5
        self.extra_service = extra_service

class CinemaHall:
    def __init__ (self, hall_name):
        self.hall_name = hall_name
        self.seat_list = []
        
    def add_seat(self, new_seat):
        self.seat_list.append(new_seat)

    def show_seat(self):
        print(f"\n--- Seats in {self.hall_name} ---")
        for seat_item in self.seat_list:
         print(f"{seat_item.seat_id:10} | {seat_item.status}")

    # def book_seat_id(self, target_id):
    #     for seat_item in self.seat_list:
    #         if seat_item.seat_id == target_id:
    #             seat_item.Book()
    #             return
    #     print(f"Seat {target_id} no found in this hall")

    # def cancel_seat_id(self, target_id):
    #     for seat_item in self.seat_list:
    #         if seat_item.seat_id == target_id:
    #             seat_item.cancel()
    #             return
    #     print(f"Seat {target_id} no found in this hall")

    def calculate_total_revenue(self):
        total_revenue = 0
        for seat_item in self.seat_list:
            if seat_item.status == "booked":
                if hasattr(seat_item, "VIP_price"):
                    total_revenue += seat_item.VIP_price
                else:
                    total_revenue += seat_item.basic_price
        print(f"Total Revenue for {self.hall_name}: {total_revenue}")
        return total_revenue

hall = CinemaHall("Main Hall")

class Movie:
    def __init__(self, title, duration, genre):
        self.title = title
        self.duration = duration
        self.genre = genre

class Screening:
    def __init__(self, movie, hall, start_time):
        self.movie = movie
        self.hall = hall
        self.start_time = start_time
        self.bookings = []

    def book_seat(self, customer, seat_id):
        for seat_item in self.hall.seat_list:
            if seat_item.seat_id == seat_id:
                if seat_item.status == "available":
                    seat_item.Book()
                    booking = Booking(
                        customer,
                        self,
                        seat_item
                    )
                    self.bookings.append(booking)
                    return booking
                else:
                    print("This seat already booked.")
                    return
        print(f"Seat {seat_id} NOT found!")


class Booking:
    def __init__(self, customer, screening, seat):
        self.customer = customer
        self.screening = screening
        self.seat = seat

class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.reservation_code = self.generate_reservation_code()

    def generate_reservation_code(self):
        return f"RES{random.randint(1000,9999)}"

# Create a cinema hall
hall = CinemaHall("Main Hall")

# ---------- Normal Seats (100) ----------
for row in "ABCDEFGHIJ":
    for number in range(1, 11):
        seat_id = f"{row}{number}"
        hall.add_seat(Seat(seat_id, 100))

# ---------- VIP Seats (40) ----------
for row in "ABCD":
    for number in range(1, 11):
        seat_id = f"VIP-{row}{number}"
        hall.add_seat(VIP_seat(seat_id, 200, "Popcorn + Drink"))

my_movie = Movie("Inception", 148, "Sci-Fi")
my_screening = Screening(my_movie, hall, "18:00")

# Create a movie
my_movie = Movie("Inception", 148, "Sci-Fi")
my_movie_2 = Movie("Interstellar", 169, "Sci-Fi")

# Create a screening
my_screening = Screening(
    my_movie,
    hall,
    "18:00"
)
my_screening_2 = Screening(
    my_movie_2,
    hall,
    "20:30"
)

# Create a customer
def create_customer():
    name = input("Enter customer name: ")

    while True:
        phone = input("Enter phone number: ")
        
        #Validation
        if phone.isdigit() and len(phone) == 11 and phone.startswith("09"):
            break
        else:
            print("Invalid phone number! Please enter a valid Iranian mobile number.\n")

    return Customer(name, phone)

# User Interface
while True:
    print("\n=== Cinema Booking System ===")
    print("1. Show seats")
    print("2. Book a seat")
    print("3. Show revenue")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        hall.show_seat()

    elif choice == "2":
        customer = create_customer()
        seat_id = input("Enter seat ID: ").upper()
        booking = my_screening.book_seat(customer, seat_id)

        if booking:
            print(f"\nSeat {seat_id} booked for {customer.name}")
            print(f"Reservation Code: {customer.reservation_code}")

    elif choice == "3":
        hall.calculate_total_revenue()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")
