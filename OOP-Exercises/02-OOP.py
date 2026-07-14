# ========================
# Customer Data Analytics
# ========================

class Customer:
    '''Represents a standard customer with basic purchase data.'''
    def __init__(self, name, age, purchase_amount):
        self.name = name
        self.age = age
        self.purchase_amount = purchase_amount
        
    def __str__(self):
        # Returns a user-friendly string representation of the object
        return f"Customer: {self.name} - Age :{self.age} - Purchasse: {self.purchase_amount}"


class VIPCustomer(Customer):
    '''Represents a premium customer inheriting from Customer with an extra discount feature.'''
    def __init__(self, name, age, purchase_amount, discount_rate = 0.15):
        # Inherit core attributes from the parent class
        super().__init__(name, age, purchase_amount)
        self.discount_rate = discount_rate
        
    def __str__(self):
        # Custom representation showing the premium VIP status and discount details
        return f"VIP: {self.name} - Age: {self.age} - Purchasse: {self.purchase_amount} - Discount: {self.discount_rate * 100}%"
    
# --- Simulated Dataset <Python List> ---
customers_data = [
    Customer ("Romina", 23, 180),
    Customer ("Maryam", 25, 98),
    Customer ("Raha", 17, 60),
    Customer ("Ali", 27, 250),
    Customer ("Yeganeh", 22, 103),
    VIPCustomer("Elnaz", 31, 390, 0.2)
    ]
print("--- High Spenders (Over $100) ---")

# --- Data Processing and Filtering Loop ---
for person in customers_data:
    if person.purchase_amount > 100:
        print(person)
    else:
        pass
