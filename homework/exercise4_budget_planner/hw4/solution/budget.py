from dataclasses import dataclass


@dataclass
class Income:
    description: str
    amount: float


@dataclass
class Expense:
    description: str
    amount: float


class Budget:

    def __init__(self) -> None:
        self._incomes: list[Income] = []
        self._expenses: list[Expense] = []

    def add_income(self, description: str, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Income amount cannot be negative or 0")

        income = Income(description, amount)
        self._incomes.append(income)

    def get_incomes(self) -> list[Income]:
        return self._incomes.copy()

    def add_expense(self, description: str, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Expense amount cannot be negative or 0")

        expenses = Expense(description, amount)
        self._expenses.append(expenses)

    def get_expenses(self) -> list[Expense]:
        return self._expenses.copy()

    def total_income(self) -> float:
        return sum(income.amount for income in self._incomes)

    def total_expense(self) -> float:
        return sum(expense.amount for expense in self._expenses)

    def remaining_budget(self) -> float:
        remaining = self.total_income() - self.total_expense()
        return remaining

    def remove_income(self, description: str) -> None:
        for income in self._incomes:
            if income.description == description:
                self._incomes.remove(income)

                return

        raise ValueError("Income description not found")

    def remove_expense(self, description: str) -> None:
        for expense in self._expenses:
            if expense.description == description:
                self._expenses.remove(expense)
                return

        raise ValueError("Expense description not found")

    def clear_all(self) -> None:
        self._incomes.clear()
        self._expenses.clear()
