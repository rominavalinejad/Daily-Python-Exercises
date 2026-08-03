# 01-OOP
## Challenge: Task Management System

1. Define a base class Task to represent a generic task with a title and a description.
2. Implement a specialized class UrgentTask that inherits from Task and includes an additional property for priority level (e.g., High, Critical).
3. Create a TaskManager class responsible for storing tasks in a central list
4. Customize the string representation (`__str__`) for both task classes to ensure a clean, human-readable format when printed.
5. Implement an interactive while loop menu that continuously prompts the user to select one of three operations:
   - Show all tasks: Display every task stored in the system.
   - Show important tasks: Dynamically filter and output only the tasks that belong to the UrgentTask type.
   - Exit: Safely terminate the program.
6. Use an 'if-elif-else' block to show an error "Invalid input" if the user type anything other than 1, 2, or 3.

# 02-OOP
## Challenge: Customer Data Analytics

1. Create a base class named 'Customer' that takes three attributes in its constructor (`__init__`): name, age, and purchase_amount.
2. Implement a __str__ dunder method inside Customer to return a clean, formatted string displaying the customer's name, age, and purchase details.
3. Create a subclass named VIPCustomer that inherits from Customer. It must accept an additional parameter discount_rate in its constructor (with a default value of 0.15) and call the parent constructor using super().
4. Override the __str__ method in VIPCustomer to return a customized string that includes the premium status and the discount rate percentage.
5. Create a simulated dataset named customers_data as a list containing at least 5-6 instances of both Customer and VIPCustomer with different purchase values.
6. Write a loop to iterate through the dataset, filtering and printing only the details of customers whose purchase_amount is strictly greater than 100.

# 03-OOP
## Challenge: Vehicle Fleet Management System
### Scenario:
A vehicle rental agency needs a system to manage its fleet of standard cars and electric vehicles (EVs). To encourage sustainable travel, the agency offers a 10% eco-discount on the daily rental cost of electric vehicles.

1. Vehicle Base Model: Represent standard vehicles with attributes for brand, model, and daily rate. Include functionality to calculate rental costs for given days and display formatted vehicle details.
2. Electric Vehicle Support: Model electric vehicles with extra properties like battery capacity, ensuring rental calculations automatically incorporate the 10% eco-discount.
3. Fleet Management: Implement a central fleet manager to register vehicles, view the entire inventory, and dynamically isolate electric vehicles.
4. Execution: Populate the fleet with sample vehicles, list all entries, and calculate 3-day rental totals for the electric fleet.
