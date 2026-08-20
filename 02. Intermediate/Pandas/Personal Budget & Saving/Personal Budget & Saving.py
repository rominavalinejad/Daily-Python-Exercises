import json
from turtle import pensize
from PIL.Image import preinit
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


# -------- DataFrame Inspection ---------

print("\nThree-Month Expenses:")
print(expenses)

print("\nDataFrame Shape:")
print(expenses.shape)

print("\nDataFrame Columns:")
print(expenses.columns)

print("\nDataFrame Info:")
expenses.info()

print("\nStatistical Summary:")
print(expenses.describe())

# -------- Filtering --------

print("\nAugust Expenses:")
print(expenses["August"])

high_august_expenses = expenses[
    expenses["August"] > 2_000_000
]

print("\nHigh August Expenses:")
print(high_august_expenses)

increased_expenses = expenses[
    expenses["August"] > expenses["June"]
]

print("\nExpenses Increased from June to August:")
print(increased_expenses)

expenses["Increase (%)"] = (
    (expenses["August"] - expenses["June"])
    / expenses["June"]
) * 100

print("\nExpense Increase Percentage:")
print(expenses[["Category", "Increase (%)"]])

# -------- Sort Expenses by Increase Percentage --------

sorted_expenses = expenses.sort_values(
    by="Increase (%)",
    ascending=False
)

print("\nExpenses Sorted by Increase:")
print(
    sorted_expenses[
        ["Category", "June", "August", "Increase (%)"]
    ]
)

# -------- Monthly Total Expenses --------

monthly_total = expenses[
    ["June", "July", "August"]
].sum()

print("\nTotal Expenses by Month:")
print(monthly_total)

# -------- Monthly Savings --------

monthly_salary = budget_config["monthly_salary"]

monthly_savings = monthly_salary - monthly_total

print("\nMonthly Savings:")
print(monthly_savings)

