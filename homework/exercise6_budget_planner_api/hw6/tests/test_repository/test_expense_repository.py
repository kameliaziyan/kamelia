from unittest.mock import Mock

from solution.repository.expense_repository import ExpenseRepository
from solution.budget_hw4_bonus import Expense


def test_create_expense() -> None:

    mock_accessor = Mock()
    mock_accessor.read.return_value = {"items": []}

    repo = ExpenseRepository(file_accessor=mock_accessor)
    expense = Expense(description="Food", amount=200, id=0)

    created = repo.create(expense)

    assert created.id == 1
    mock_accessor.write.assert_called_once()


def test_get_all_expenses() -> None:
    mock_accessor = Mock()
    mock_accessor.read.return_value = {
        "items": [{"description": "Taxi", "amount": 50, "id": 1}]
    }

    repo = ExpenseRepository(file_accessor=mock_accessor)

    result = repo.get_all()

    assert len(result) == 1
    assert result[0].description == "Taxi"
    assert result[0].amount == 50
    assert result[0].id == 1


def test_delete_expense() -> None:

    mock_accessor = Mock()

    mock_accessor.read.return_value = {
        "items": [{"description": "Taxi", "amount": 50, "id": 1}]
    }

    repo = ExpenseRepository(file_accessor=mock_accessor)

    repo.delete(1)
    mock_accessor.write.assert_called_once()
