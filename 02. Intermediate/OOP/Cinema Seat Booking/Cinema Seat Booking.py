'''
Cinema Seat Booking System (OOP core)
'''
from tokenize import generate_tokens
from turtle import pensize


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
        print(f"--- Seats {self.hall_name} ---")
        for seat_item in self.seat_list:
            print(
            f"Seat ID: {seat_item.seat_id}\n"
            f"Status: {seat_item.status}"
            )

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
    def __init__(self, name, phone, reservation_code):
        self.name = name
        self.phone = phone
        self.reservation_code = reservation_code

# Create a cinema hall
hall = CinemaHall("Main Hall")
my_movie = Movie("Inception", 148, "Sci-Fi")
my_screening = Screening(my_movie, hall, "18:00")
my_customer = Customer("Romina","09128350102","RES001")

# Create regular and VIP seats
s1 = Seat("A1", 100)
s2 = Seat("A2", 100)
v1 = VIP_seat("V1", 200, "Popcorn")

# Add seats to the cinema hall
hall.add_seat(s1)
hall.add_seat(s2)
hall.add_seat(v1)

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
my_customer = Customer(
    "Romina",
    "09128350102",
    "RES001"
)
my_customer_2 = Customer(
    "Ali",
    "09351234567",
    "RES002"
)

# Display seats
hall.show_seat

# Book seat A1
my_screening.book_seat(my_customer, "A1")

# Book VIP seat V1
my_screening.book_seat(my_customer, "A1")

my_screening_2.book_seat(my_customer_2, "V1")

print("\n--- Bookings ---")

for booking in my_screening.bookings:
    print(
        f"Customer: {booking.customer.name}\n"
        f"Movie: {booking.screening.movie.title}\n"
        f"Seat: {booking.seat.seat_id}\n"
        f"Time: {booking.screening.start_time}\n"
    )
print("\n--- Bookings ---")

for booking in my_screening_2.bookings:
    print(
        f"Customer: {booking.customer.name}\n"
        f"Movie: {booking.screening.movie.title}\n"
        f"Seat: {booking.seat.seat_id}\n"
        f"Time: {booking.screening.start_time}\n"
    )

# Calculate total revenue
hall.calculate_total_revenue()
