# 01-Function
## Challenge: Payroll and Tax Calculation System

1. Create a function named 'calculate_salary' that takes two parameters: 'base_hours' and 'hourly_rate'. It must calculate the total gross salary and RETURN the value.
2. Create a second function named 'calculate_tax' that takes 'gross_salary' as a parameter, calculates a 10% tax deduction, and RETURN the tax amount.
3. In the main execution block, use a 'while True' loop to dynamically prompt the operator for the number of days worked, daily shift hours, and hourly rate.
4. Call both functions sequentially, using the output of the first function as the input for the second function.
5. Include robust error handling to ensure all user inputs are numeric, using a 'try-except' block to prevent system crashes.
6. Print a structured, professional receipt showing the Total Hours, Gross Salary, Tax Deduction, and Net Salary (Gross minus Tax) using string formatting.
7. Provide an option to type 'F' at any input prompt to safely shut down the operator console.
