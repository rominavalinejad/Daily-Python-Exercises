# =======================
# Task Management System
# =======================

# Base class representing a standard task
class Task():
    def __init__(self, title, description):
        self.title = title
        self.description = description
    
    # Returns a clean string format when the task object is printed
    def __str__(self):
        return (f"{self.title}, {self.description}")

# Child class inheriting from Task with an extra priority feature
class UrgentTask(Task):
    def __init__ (self, title, description, priority = "High"):
        super().__init__(title, description)
        self.priority = priority
    
    # Custom string format for urgent tasks
    def __str__(self):
        return (f"{self.title}, {self.description}")

# Class to manage a collection of tasks
class TaskManager:
    def __init__(self):
        # Central list to store all tasks
        self.task = []
    
    # Method to add a new task object to the system
    def add_task(self, task):
        self.task.append(task)
        pass
    
    # Method to loop through and print all stored tasks
    def show_all_tasks(self):
        for task in self.task:
            print(task)

# Interactive Menu System
manager = TaskManager()

# Default tasks sample data
manager.add_task(Task("Python exercises", "GitHub Upload"))
manager.add_task(Task("Read a book", "Cook dinner"))
manager.add_task(Task("Go shopping", "Watch an independent animation"))
manager.add_task(UrgentTask("English exam", "Push the final OOP code", priority="Critical"))

while True:
    print("\n" + "="*30)
    print("      TASK MANAGER      ")
    print("="*30)
    print("1. Show all tasks")
    print("2. Mark a task as done")
    print("3. Exit")
    print("="*30)
    
    choice = input("Enter your choice (1-3): ")
    
    # Option 1: Displays everything in the list
    if choice == "1":
        print("\n--- All Tasks ---")
        manager.show_all_tasks()
    
    # Option 2: filter and display only urgent tasks
    elif choice == "2":
        print("\n--- Important task to complete ---")
        for task in manager.task:
            if isinstance(task, UrgentTask):
                print(task)
    
    # Option 3: Safely breaks the loop
    elif choice == "3":
        print("Shut down.")
        break
    
    # Input Validation
    else:
        print("Invalid input!\nPlease enter 1, 2, or 3.")
