import pytest
from solution.budget import Budget


def test_add_income() -> None:
    budget = Budget()
    budget.add_income("Salary", 5000)

    assert len(budget.incomes) == 1
    assert budget.total_income() == 5000


def test_remaining_budget() -> None:
    budget = Budget()
    budget.add_income("Salary", 5000)
    budget.add_expense("Rent", 1500)

    assert budget.remaining_budget == 3500


def test_remove_expense() -> None:
    budget = Budget()
    budget.add_expense("Rent", 1500)

    budget.remove("Rent", "expense")

    assert budget.total_expense() == 0
    assert len(budget.expenses) == 0


def test_remove_notfound() -> None:
    budget = Budget()

    with pytest.raises(ValueError):
        budget.remove("Nonexistent", "income")


def test_add_income_negative() -> None:
    budget = Budget()

    with pytest.raises(ValueError):
        budget.add_income("Salary", -100)


def test_add_income_zero() -> None:
    budget = Budget()

    with pytest.raises(ValueError):
        budget.add_income("Salary", 0)
