from dataclasses import dataclass
from solution.repository.income_repository import IncomeRepository
from solution.repository.expense_repository import ExpenseRepository

INCOME = "income"
EXPENSE = "expense"

INVALID_TYPE = "Invalid item type"


@dataclass
class Income:
    """Data class that  represents a single income source."""

    description: str
    amount: float
    id: int


@dataclass
class Expense:
    """Data class that  represents a single expense."""

    description: str
    amount: float
    id: int


class Budget:
    """Class that manages income and expense entries."""

    def __init__(self) -> None:
        self._income_repository = IncomeRepository()
        self._expense_repository = ExpenseRepository()

    def add(self, description: str, amount: float, item_type: str) -> None:
        """Add income or expense entry."""
        amount = float(amount)

        if amount <= 0:
            raise ValueError("Amount cannot be negative or 0 ")

        if item_type == INCOME:

            income = Income(description=description, amount=amount, id=0)
            self._income_repository.create(income)

        elif item_type == EXPENSE:

            expense = Expense(description=description, amount=amount, id=0)
            self._expense_repository.create(expense)

        else:
            raise ValueError(INVALID_TYPE)

    @property
    def incomes(self) -> list[Income]:
        """Return all income  entries ."""

        return self._income_repository.get_all()

    @property
    def expenses(self) -> list[Expense]:
        """Return all expense  entries."""
        return self._expense_repository.get_all()

    def total(self, item_type: str) -> float:
        """Return total income  or expense."""

        if item_type == INCOME:
            return sum(income.amount for income in self._income_repository.get_all())

        if item_type == EXPENSE:
            return sum(expense.amount for expense in self._expense_repository.get_all())

        raise ValueError(INVALID_TYPE)

    @property
    def remaining_budget(self) -> float:
        """Return the remaining budget."""
        return self.total(INCOME) - self.total(EXPENSE)

    def remove(self, item_id: int, item_type: str) -> None:
        """Remove an income or expense by its ID."""

        if item_type == INCOME:
            self._income_repository.delete(item_id)
            return

        if item_type == EXPENSE:
            self._expense_repository.delete(item_id)
            return

        raise ValueError(INVALID_TYPE)

    def clear_all(self) -> None:
        """Remove all income and expense entries ."""
        self._income_repository.clear()

        self._expense_repository.clear()

    def summary(self) -> dict[str, float]:
        """Return a summary of the budget."""

        return {
            "total_income": self.total(INCOME),
            "total_expense": self.total(EXPENSE),
            "remaining_budget": self.remaining_budget,
        }
