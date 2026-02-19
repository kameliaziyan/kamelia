from dataclasses import dataclass

INCOME = "income"
EXPENSE = "expense"
INVALID_TYPE = "Invalid item type"


@dataclass
class Income:
    """Represents a single income source with description and amount."""

    description: str
    amount: float
    id: int


@dataclass
class Expense:
    """Represents a single expense item with description and amount."""

    description: str
    amount: float
    id: int


class Budget:
    """Manage income and expense entries."""

    def __init__(self) -> None:
        self._incomes: list[Income] = []
        self._expenses: list[Expense] = []
        self._id_counter: int = 1

    def add(self, description: str, amount: float, item_type: str) -> None:
        """Add income or expense entry."""
        amount = float(amount)

        if amount <= 0:
            raise ValueError("Amount cannot be negative or 0")

        new_id = self._id_counter
        self._id_counter += 1

        if item_type == INCOME:
            self._incomes.append(Income(description, amount, new_id))
        elif item_type == EXPENSE:
            self._expenses.append(Expense(description, amount, new_id))
        else:
            raise ValueError("")

    @property
    def incomes(self) -> list[Income]:
        """Return a copy of all income entries."""
        return self._incomes.copy()

    @property
    def expenses(self) -> list[Expense]:
        """Return a copy of all expense entries."""
        return self._expenses.copy()

    def total(self, item_type: str) -> float:
        """Return total income or expense."""
        if item_type == INCOME:
            return sum(income.amount for income in self._incomes)

        if item_type == EXPENSE:
            return sum(expense.amount for expense in self._expenses)

        raise ValueError("")

    @property
    def remaining_budget(self) -> float:
        """Return the remaining budget."""
        return self.total(INCOME) - self.total(EXPENSE)

    def remove(self, item_id: int, item_type: str) -> None:
        """Remove an income or expense by its description."""

        if item_type == INCOME:
            for income in self._incomes:
                if income.id == item_id:
                    self._incomes.remove(income)
                    return
            raise ValueError("Income not found")

        if item_type == EXPENSE:
            for expense in self._expenses:
                if expense.id == item_id:
                    self._expenses.remove(expense)
                    return
            raise ValueError("Expense not found")

        raise ValueError("")

    def clear_all(self) -> None:
        """Remove all income and expense entries from the budget."""

        self._incomes.clear()
        self._expenses.clear()
        self._id_counter = 1

    def summary(self) -> dict[str, float]:
        """Return a summary of the budget."""
        return {
            "total_income": self.total(INCOME),
            "total_expense": self.total(EXPENSE),
            "remaining_budget": self.remaining_budget,
        }
