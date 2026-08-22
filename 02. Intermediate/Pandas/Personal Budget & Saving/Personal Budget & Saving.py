import json

import pandas as pd


# -------- Constants --------

MONTHS = ("June", "July", "August")


# -------- Load Budget Configuration --------

def load_budget_config(file_path: str) -> dict:
    """Load budget configuration from a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)


# -------- Load Monthly Expenses --------

def load_monthly_expenses() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Load expense data for June, July, and August."""
    june = pd.read_excel("Summer_June.xlsx")
    july = pd.read_excel("Summer_July.xlsx")
    august = pd.read_excel("Summer_August.xlsx")

    return june, july, august


# -------- Prepare Expenses --------

def prepare_expenses(
    june: pd.DataFrame,
    july: pd.DataFrame,
    august: pd.DataFrame,
) -> pd.DataFrame:
    """Rename monthly columns and merge all expense data."""
    june = june.rename(columns={"Actual Expense": "June"})
    july = july.rename(columns={"Actual Expense": "July"})
    august = august.rename(columns={"Actual Expense": "August"})

    expenses = pd.merge(june, july, on="Category")
    expenses = pd.merge(expenses, august, on="Category")

    return expenses


# -------- Analyze Expenses --------

def analyze_expenses(expenses: pd.DataFrame) -> pd.DataFrame:
    """Calculate expense increase from June to August."""
    expenses = expenses.copy()

    expenses["Increase (%)"] = (
        (expenses["August"] - expenses["June"])
        / expenses["June"]
    ) * 100

    return expenses


# -------- Calculate Savings --------

def calculate_savings(
    expenses: pd.DataFrame,
    monthly_salary: float,
) -> tuple[pd.Series, pd.Series]:
    """Calculate total monthly expenses and monthly savings."""
    monthly_total = expenses[list(MONTHS)].sum()
    monthly_savings = monthly_salary - monthly_total

    return monthly_total, monthly_savings


# -------- Check Expense Warning --------

def check_expense_warning(
    category: str,
    expense_values: pd.Series,
    budget_config: dict,
) -> tuple[float, pd.Series]:
    """Check whether expenses exceed the configured warning limit."""
    category_config = budget_config["expenses"][category]

    expected_expense = category_config["expected"]
    warning_threshold = category_config["warning_threshold"]

    warning_limit = expected_expense * (1 + warning_threshold / 100)
    warnings = expense_values > warning_limit

    return warning_limit, warnings


# -------- Main Program --------

def main() -> None:
    budget_config = load_budget_config("budget_config.json")

    june, july, august = load_monthly_expenses()

    expenses = prepare_expenses(june, july, august)
    expenses = analyze_expenses(expenses)

    monthly_salary = budget_config["monthly_salary"]

    monthly_total, monthly_savings = calculate_savings(
        expenses,
        monthly_salary,
    )


if __name__ == "__main__":
    main()