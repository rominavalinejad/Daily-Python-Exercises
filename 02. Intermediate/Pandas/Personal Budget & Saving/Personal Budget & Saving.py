import json
from pathlib import Path

import pandas as pd


# -------- Constants --------

MONTHS = ("June", "July", "August")

# Folder where this script itself lives — used so file paths work
# regardless of the current working directory the script is run from.
BASE_DIR = Path(__file__).resolve().parent


# -------- Load Budget Configuration --------

def load_budget_config(file_path: str) -> dict:
    """Load budget configuration from a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)


# -------- Load Monthly Expenses --------

def load_monthly_expenses() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Load expense data for June, July, and August."""
    june = pd.read_excel(BASE_DIR / "Summer_June.xlsx")
    july = pd.read_excel(BASE_DIR / "Summer_July.xlsx")
    august = pd.read_excel(BASE_DIR / "Summer_August.xlsx")

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


# -------- Build Warnings Table --------

def build_warnings_table(
    expenses: pd.DataFrame,
    budget_config: dict,
) -> pd.DataFrame:
    """Run the warning check for every category and every month."""
    rows = []

    for _, row in expenses.iterrows():
        category = row["Category"]
        expense_values = row[list(MONTHS)]

        warning_limit, warnings = check_expense_warning(
            category,
            expense_values,
            budget_config,
        )

        rows.append(
            {
                "Category": category,
                "Warning Limit": warning_limit,
                **{f"{month} Over Limit": bool(warnings[month]) for month in MONTHS},
            }
        )

    return pd.DataFrame(rows)


# -------- Print Report --------

def print_report(
    expenses: pd.DataFrame,
    warnings_table: pd.DataFrame,
    monthly_total: pd.Series,
    monthly_savings: pd.Series,
    saving_goal: float,
) -> None:
    """Print a readable summary of the budget analysis to the console."""
    print("=" * 60)
    print("EXPENSES BY CATEGORY (June -> August)")
    print("=" * 60)
    print(
        expenses[["Category", *MONTHS, "Increase (%)"]]
        .round(1)
        .to_string(index=False)
    )

    print()
    print("=" * 60)
    print("WARNING CHECK (expense above expected + threshold)")
    print("=" * 60)
    print(warnings_table.round(0).to_string(index=False))

    print()
    print("=" * 60)
    print("MONTHLY TOTALS & SAVINGS")
    print("=" * 60)
    for month in MONTHS:
        status = "OK" if monthly_savings[month] >= saving_goal else "BELOW GOAL"
        print(
            f"{month:<10} Total Expenses: {monthly_total[month]:>12,.0f}  "
            f"Savings: {monthly_savings[month]:>12,.0f}  [{status}]"
        )

    print()
    avg_savings = monthly_savings.mean()
    print(f"Average monthly savings : {avg_savings:,.0f}")
    print(f"Saving goal             : {saving_goal:,.0f}")
    if avg_savings >= saving_goal:
        print("Overall: You are meeting your saving goal on average. ✅")
    else:
        print("Overall: You are falling short of your saving goal on average. ⚠️")


# -------- Save Report --------

def save_report(
    expenses: pd.DataFrame,
    warnings_table: pd.DataFrame,
    output_path: str | Path = None,
) -> None:
    """Save the expense analysis and warning check to an Excel file."""
    if output_path is None:
        output_path = BASE_DIR / "Budget_Report.xlsx"

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        expenses.to_excel(writer, sheet_name="Expenses", index=False)
        warnings_table.to_excel(writer, sheet_name="Warnings", index=False)

    print(f"\nReport saved to: {output_path}")


# -------- Main Program --------

def main() -> None:
    budget_config = load_budget_config(BASE_DIR / "budget_config.json")

    june, july, august = load_monthly_expenses()

    expenses = prepare_expenses(june, july, august)
    expenses = analyze_expenses(expenses)

    monthly_salary = budget_config["monthly_salary"]
    saving_goal = budget_config["saving_goal"]

    monthly_total, monthly_savings = calculate_savings(
        expenses,
        monthly_salary,
    )

    warnings_table = build_warnings_table(expenses, budget_config)

    print_report(
        expenses,
        warnings_table,
        monthly_total,
        monthly_savings,
        saving_goal,
    )

    save_report(expenses, warnings_table)


if __name__ == "__main__":
    main()
