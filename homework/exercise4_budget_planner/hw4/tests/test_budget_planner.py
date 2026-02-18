import pytest
from solution.budget import Budget


def test_add_expense() -> None:
    budget = Budget()
    budget.add_expense("Rent", 1500)

    assert len(budget.expenses) == 1
    assert budget.total_expense() == 1500


def test_expense_negative() -> None:
    budget = Budget()

    with pytest.raises(ValueError):
        budget.add_expense("Rent", -100)


def test_expense_zero() -> None:
    budget = Budget()

    with pytest.raises(ValueError):
        budget.add_expense("Rent", 0)


def test_total_expense() -> None:
    budget = Budget()
    budget.add_expense("Rent", 1000)
    budget.add_expense("Food", 500)

    assert budget.total_expense() == 1500


def test_remove_income() -> None:
    budget = Budget()
    budget.add_income("Salary", 5000)

    budget.remove("Salary", "income")

    assert budget.total_income() == 0
    assert len(budget.incomes) == 0


def test_invalid_type() -> None:
    budget = Budget()

    with pytest.raises(ValueError):
        budget.remove("Salary", "invalid")


def test_clear_all() -> None:
    budget = Budget()
    budget.add_income("Salary", 5000)
    budget.add_expense("Rent", 1500)

    budget.clear_all()

    assert len(budget.incomes) == 0
    assert len(budget.expenses) == 0
    assert budget.remaining_budget == 0
