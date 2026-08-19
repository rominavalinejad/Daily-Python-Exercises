import json
import pandas as pd


# -------- JSON - Load Budget Configuration --------

with open("budget_config.json", "r") as file:
    budget_config = json.load(file)

print("Monthly Salary:", budget_config["monthly_salary"])
print("Saving Goal:", budget_config["saving_goal"])

print(
    "Electricity Budget:",
    budget_config["expenses"]["Electricity"]["expected"]
)

print(
    "Electricity Warning:",
    budget_config["expenses"]["Electricity"]["warning_threshold"]
)


# -------- EXCEL - Load Monthly Expenses --------

june_expenses = pd.read_excel("Summer_June.xlsx")
july_expenses = pd.read_excel("Summer_July.xlsx")
august_expenses = pd.read_excel("Summer_August.xlsx")

# -------- Display Monthly Expenses --------

print("\nJune Expenses:")
print(june_expenses)

print("\nJuly Expenses:")
print(july_expenses)

print("\nAugust Expenses:")
print(august_expenses)

# -------- Rename Expense Columns --------

june_expenses = june_expenses.rename(
    columns={"Actual Expense": "June"}
)

july_expenses = july_expenses.rename(
    columns={"Actual Expense": "July"}
)

august_expenses = august_expenses.rename(
    columns={"Actual Expense": "August"}
)

# -------- Merge Monthly Data --------

expenses = pd.merge(
    june_expenses,
    july_expenses,
    on="Category"
)

expenses = pd.merge(
    expenses,
    august_expenses,
    on="Category"
)


# -------- Display Three-Month Expenses ---------

print("\nThree-Month Expenses:")
print(expenses)