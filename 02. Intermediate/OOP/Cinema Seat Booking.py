'''
Cinema Seat Booking System (OOP core)
'''
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
