'''
Vehicle Fleet Management System
'''

class Vehicle:
    def __init__(self, brand, model, daily_rate):
        self.brand = brand
        self.model = model
        self.daily_rate = daily_rate

    def calculate_rental_cost(self, days):
        return self.daily_rate * days

    def __str__(self):
        return f"{self.brand} {self.model} (${self.daily_rate}/day)"


class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, daily_rate, battery_capacity):
        super().__init__(brand, model, daily_rate)
        self.battery_capacity = battery_capacity

    def calculate_rental_cost(self, days):
        base_cost = super().calculate_rental_cost(days)
        return base_cost * 0.90  # Apply 10% Discount

    def __str__(self):
        return f"{super().__str__()} [Battery: {self.battery_capacity} kWh]"


class FleetManager:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def show_all_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle)

    def get_electric_vehicles(self):
        return [v for v in self.vehicles if isinstance(v, ElectricVehicle)]


# --- Test Code ---
if __name__ == "__main__":
    fleet = FleetManager()

    # Create vehicle instances
    v1 = Vehicle("Toyota", "Camry", 50)
    v2 = Vehicle("Ford", "Mustang", 80)
    ev1 = ElectricVehicle("Tesla", "Model 3", 100, 75)
    ev2 = ElectricVehicle("Nissan", "Leaf", 60, 40)

    # Add vehicles to the fleet manager
    fleet.add_vehicle(v1)
    fleet.add_vehicle(v2)
    fleet.add_vehicle(ev1)
    fleet.add_vehicle(ev2)

    # Display all vehicles
    print("--- All Vehicles in Fleet ---")
    fleet.show_all_vehicles()

    # Filter electric vehicles and calculate discounted rental cost
    print("\n--- Electric Vehicles (3 Days Rental with 10% Discount) ---")
    for ev in fleet.get_electric_vehicles():
        cost = ev.calculate_rental_cost(days=3)
        print(f"{ev} -> 3 Days Total: ${cost:.2f}")
