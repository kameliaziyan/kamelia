from unittest.mock import Mock
from solution.repository.income_repository import IncomeRepository
from solution.budget_hw4_bonus import Income

def test_create_income() -> None:

    mock_accessor = Mock()
    mock_accessor.read.return_value = {"item": []}

    repo = IncomeRepository(file_accessor= mock_accessor)
    income = Income(description= "Salary", amount= 500, id= 0)
    created = repo.create(income)
    assert created.id == 1
    mock_accessor.write.assert_called_once()


def test_get_all() -> None:
    mock_accessor = Mock()
    mock_accessor.read.return_value = {
        "items": [{"description": "Salary", "amount": 100, "id": 1}]
    }

    repo = IncomeRepository(file_accessor= mock_accessor)
    result = repo.get_all()

    assert len(result) == 1
    assert result[0].description == "Salary"
    assert result[0].amount == 100
    assert result[0].id == 1


def test_delete_income() -> None:
    mock_accessor = Mock()

    mock_accessor.read.return_value = {
        "items": [{"description": "Salary", "amount": 100, "id": 1}]
    }
    repo = IncomeRepository(file_accessor= mock_accessor)
    repo.delete(1)
    mock_accessor.write.assert_called_once()


