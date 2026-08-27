"""
Unit tests for "Personal Budget & Saving.py".

Run with:
    pytest test_budget.py -v
"""

import importlib.util
import os
import sys

import pandas as pd
import pytest

# --- Load the module even though its filename has spaces / "&" in it ---
MODULE_PATH = os.path.join(
    os.path.dirname(__file__), "Personal Budget & Saving.py"
)
spec = importlib.util.spec_from_file_location("budget_module", MODULE_PATH)
budget = importlib.util.module_from_spec(spec)
sys.modules["budget_module"] = budget
spec.loader.exec_module(budget)


# -------- Fixtures --------

@pytest.fixture
def budget_config():
    return {
        "monthly_salary": 30_000_000,
        "saving_goal": 10_000_000,
        "expenses": {
            "Rent": {"expected": 10_000_000, "warning_threshold": 10},
            "Food": {"expected": 5_000_000, "warning_threshold": 15},
        },
    }


@pytest.fixture
def sample_expenses():
    return pd.DataFrame(
        {
            "Category": ["Rent", "Food"],
            "June": [10_000_000, 5_200_000],
            "July": [10_000_000, 5_700_000],
            "August": [10_000_000, 6_300_000],
        }
    )


# -------- load_budget_config --------

def test_load_budget_config_reads_json(tmp_path):
    config_path = tmp_path / "config.json"
    config_path.write_text('{"monthly_salary": 1000, "saving_goal": 100}')

    result = budget.load_budget_config(str(config_path))

    assert result == {"monthly_salary": 1000, "saving_goal": 100}


# -------- prepare_expenses --------

def test_prepare_expenses_merges_and_renames_columns():
    june = pd.DataFrame({"Category": ["Rent"], "Actual Expense": [10_000_000]})
    july = pd.DataFrame({"Category": ["Rent"], "Actual Expense": [10_000_000]})
    august = pd.DataFrame({"Category": ["Rent"], "Actual Expense": [11_000_000]})

    result = budget.prepare_expenses(june, july, august)

    assert list(result.columns) == ["Category", "June", "July", "August"]
    assert result.loc[0, "August"] == 11_000_000


# -------- analyze_expenses --------

def test_analyze_expenses_computes_increase_percentage(sample_expenses):
    result = budget.analyze_expenses(sample_expenses)

    # Rent: no change -> 0%
    assert result.loc[0, "Increase (%)"] == 0

    # Food: (6,300,000 - 5,200,000) / 5,200,000 * 100
    expected_increase = (6_300_000 - 5_200_000) / 5_200_000 * 100
    assert result.loc[1, "Increase (%)"] == pytest.approx(expected_increase)


# -------- calculate_savings --------

def test_calculate_savings_totals_and_subtracts_from_salary(sample_expenses):
    monthly_total, monthly_savings = budget.calculate_savings(
        sample_expenses, monthly_salary=30_000_000
    )

    assert monthly_total["June"] == 15_200_000
    assert monthly_savings["June"] == 30_000_000 - 15_200_000
    assert monthly_savings["August"] == 30_000_000 - 16_300_000


# -------- check_expense_warning --------

def test_check_expense_warning_flags_values_over_limit(budget_config):
    expense_values = pd.Series(
        {"June": 5_200_000, "July": 5_700_000, "August": 6_300_000}
    )

    warning_limit, warnings = budget.check_expense_warning(
        "Food", expense_values, budget_config
    )

    # expected=5,000,000, threshold=15% -> limit = 5,750,000
    assert warning_limit == pytest.approx(5_750_000)
    assert bool(warnings["June"]) is False   # 5,200,000 <= 5,750,000
    assert bool(warnings["July"]) is False   # 5,700,000 <= 5,750,000
    assert bool(warnings["August"]) is True  # 6,300,000 >  5,750,000


def test_check_expense_warning_no_warning_when_within_limit(budget_config):
    expense_values = pd.Series(
        {"June": 10_000_000, "July": 10_000_000, "August": 10_000_000}
    )

    warning_limit, warnings = budget.check_expense_warning(
        "Rent", expense_values, budget_config
    )

    assert warning_limit == pytest.approx(11_000_000)
    assert not warnings.any()


# -------- build_warnings_table --------

def test_build_warnings_table_has_one_row_per_category(sample_expenses, budget_config):
    result = budget.build_warnings_table(sample_expenses, budget_config)

    assert len(result) == len(sample_expenses)
    assert set(result["Category"]) == {"Rent", "Food"}
    assert "August Over Limit" in result.columns
    # Food in August (6,300,000) exceeds its 5,750,000 limit
    assert bool(result.loc[result["Category"] == "Food", "August Over Limit"].iloc[0]) is True


# -------- save_report --------

def test_save_report_creates_excel_with_two_sheets(tmp_path, sample_expenses, budget_config):
    output_path = tmp_path / "report.xlsx"
    warnings_table = budget.build_warnings_table(sample_expenses, budget_config)

    budget.save_report(sample_expenses, warnings_table, output_path=str(output_path))

    assert output_path.exists()
    sheets = pd.ExcelFile(output_path).sheet_names
    assert sheets == ["Expenses", "Warnings"]
