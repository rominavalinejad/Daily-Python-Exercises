'''
Cinema Seat Booking System (OOP core)
'''
from turtle import pensize


class seat:
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

    def book(self):
        if self.status == "available":
            self.status = "booked"
            print ("This seat is now booked successfully")
        elif self.status == "in_progress":
            print("This seat is currently in progress by someone else. Try later!")
        elif self.status == "booked":
            print("This seat is already booked")

    def cancel(self):
        if self.status == "booked":
            self.status = "available"
            print("Booking calnceled successfully")
        else:
            print("This seat is NOT booked yet!")

class VIP_seat(seat):
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
            print(f"Seat ID: {seat_item.seat_id}\nStatus: {seat_item.status}")

    def book_seat_id(self, target_id):
        for seat_item in self.seat_list:
            if seat_item.seat_id == target_id:
                seat_item.book()
                return
        print(f"Seat {target_id} no found in this hall")

    def cancel_seat_id(self, target_id):
        for seat_item in self.seat_list:
            if seat_item.seat_id == target_id:
                seat_item.cancel()
                return
        print(f"Seat {target_id} no found in this hall")

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

'''Create a cinema hall instance'''
hall = CinemaHall("Main Hall")

'''Create regular and VIP seats'''
s1 = seat("A1", 100)
s2 = seat("A2", 100)
v1 = VIP_seat("V1", 200, "Popcorn")

''' Add seats to the cinema hall'''
hall.add_seat(s1)
hall.add_seat(s2)
hall.add_seat(v1)

'''Display all seats and their initial status'''
hall.show_seat

''' Book seat A1 and VIP seat V1'''
hall.book_seat_id("A1")
hall.book_seat_id("V1")

'''Calculate total revenue for all booked seats'''
hall.calculate_total_revenue()
