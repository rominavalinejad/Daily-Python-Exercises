import json
import pandas as pd
import numpy as np

# -------- Load Budget Configuration *Json --------

def load_budget_config(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# -------- Load Monthly Expenses *Exel --------

def load_monthly_expenses():
    june = pd.read_excel("Summer_June.xlsx")
    july = pd.read_excel("Summer_July.xlsx")
    august = pd.read_excel("Summer_August.xlsx")

    return june, july, august

# -------- Prepare Expenses --------

def prepare_expenses(june, july, august):
    june = june.rename(columns={"Actual Expense": "June"})
    july = july.rename(columns={"Actual Expense": "July"})
    august = august.rename(columns={"Actual Expense": "August"})

    # Merge Monthly Data
    expenses = pd.merge(june, july, on="Category")
    expenses = pd.merge(expenses, august, on="Category")

    return expenses

# -------- Analyze Expenses --------

def analyze_expenses(expenses):
    expenses = expenses.copy()

    expenses["Increase (%)"] = (
        (expenses["August"] - expenses["June"])
        / expenses["June"]
    ) * 100

    return expenses

# -------- Calculate Savings --------

def calculate_savings(expenses, monthly_salary):
    monthly_total = expenses[
        ["June", "July", "August"]
    ].sum()

    monthly_savings = monthly_salary - monthly_total

    return monthly_total, monthly_savings

# -------- Check Expense Warning --------

def check_expense_warning(category, expense_values, budget_config):
    config = budget_config["expenses"][category]

    expected = config["expected"]
    threshold = config["warning_threshold"]

    warning_limit = expected * (1 + threshold / 100)

    warnings = expense_values > warning_limit

    return warning_limit, warnings

# -------- Main Program --------

def main():
    budget_config = load_budget_config("budget_config.json")

    june, july, august = load_monthly_expenses()

    expenses = prepare_expenses(
        june,
        july,
        august
    )

    expenses = analyze_expenses(expenses)

    monthly_salary = budget_config["monthly_salary"]

    monthly_total, monthly_savings = calculate_savings(
        expenses,
        monthly_salary
    )


if __name__ == "__main__":
    main()
    