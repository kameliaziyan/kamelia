import pytest
from solution.budget import Budget


def test_add_expense() -> None:
    budget = Budget()
    budget.add("Rent", 1500, "expense")

    assert len(budget.expenses) == 1
    assert budget.total("expense") == 1500


def test_expense_negative() -> None:
    budget = Budget()

    with pytest.raises(ValueError):
        budget.add("Rent", -100, "expense")


def test_expense_zero() -> None:
    budget = Budget()

    with pytest.raises(ValueError):
        budget.add("Rent", 0, "expense")


def test_total_expense() -> None:
    budget = Budget()
    budget.add("Rent", 1000, "expense")
    budget.add("Food", 500, "expense")

    assert budget.total("expense") == 1500


def test_remove_income() -> None:
    budget = Budget()
    budget.add("Salary", 5000, "income")

    income_id = budget.incomes[0].id
    budget.remove(income_id, "income")

    assert budget.total("income") == 0
    assert len(budget.incomes) == 0


def test_invalid_type() -> None:
    budget = Budget()

    with pytest.raises(ValueError):
        budget.remove(1, "invalid")


def test_clear_all() -> None:
    budget = Budget()
    budget.add("Salary", 5000, "income")
    budget.add("Rent", 1500, "expense")

    budget.clear_all()

    assert len(budget.incomes) == 0
    assert len(budget.expenses) == 0
    assert budget.remaining_budget == 0
