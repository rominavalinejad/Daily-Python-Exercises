# =======================================================
# Payroll and Tax Calculation System - Enterprise Edition
# =======================================================

# Phase 1: Processing Engine & Logic Execution
def calculate_salary(base_hours, hourly_rate):
    res = base_hours * hourly_rate
    return res

def calculate_tax(gross_salary):
    tax = gross_salary * 0.1
    return tax

# Phase 2: System Control & Operator Input Management
print("PAYROLL SYSTEM INITIALIZED")
print("Type 'F' to shut down.")
print("-" * 30)

while True:
    # Get days worked
    days_input = input("\nEnter total days worked: ").strip()
    if days_input.lower() == 'f':
        print("System shutting down safely.")
        break

    hours_input = input("Enter daily working hours: ").strip()
    if hours_input.lower() == 'f':
        print("System shutting down safely.")
        break

    rate_input = input("Enter hourly rate: ").strip()
    if rate_input.lower() == 'f':
        print("System shutting down safely.")
        break
    # Error handling: ensure all inputs are numeric
    try:
        days = float(days_input)
        hours_per_day = float(hours_input)
        rate = float(rate_input)
    except ValueError:
        print("Invalid input!❌ Please enter numbers only.")
        continue
    # Calculate total hours automatically
    total_hours = days * hours_per_day
    # Process metrics using functions
    gross = calculate_salary(total_hours, rate)
    tax = calculate_tax(gross)
    net_salary = gross - tax
    # Display structured professional receipt
    print("-" *30)
    print(f"💠Total Hours  : {total_hours:>10.1f}💠")
    print(f"💠Gross Salary : {gross:>10.2f}💠")
    print(f"💠Tax Deduction: {tax:>10.2f}💠")
    print(f"💠Net Salary   : {net_salary:>10.2f}💠")
    print("-" *30)
