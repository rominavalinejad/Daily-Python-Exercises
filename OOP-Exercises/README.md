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
6. Use an 'if-elif-else' block to show an error "Invalid input" if the user typee anything other than 1, 2, or 3.
