from dataclasses import asdict
from typing import TYPE_CHECKING, List, Dict, Any, Optional

from solution.repository.file_accessor import JsonFileAccessor

if TYPE_CHECKING:
    from solution.budget_hw4_bonus import Expense


DATA_FILE = "data/expenses.json"


class ExpenseRepository:
    def __init__(
        self,
        file_accessor: Optional[JsonFileAccessor] = None,
    ) -> None:
        self.file_accessor: JsonFileAccessor = (
            file_accessor if file_accessor else JsonFileAccessor(DATA_FILE)
        )

    def create(self, expense: "Expense") -> "Expense":
        from solution.budget_hw4_bonus import Expense

        items = self._read_items()
        expense.id = self._generate_id(items)
        items.append(asdict(expense))
        self._write_items(items)
        return expense

    def get_all(self) -> List["Expense"]:
        from solution.budget_hw4_bonus import Expense

        items = self._read_items()
        expenses: List[Expense] = []

        for item in items:
            expenses.append(Expense(**item))

        return expenses

    def delete(self, expense_id: int) -> None:
        items = self._read_items()

        updated_items = [item for item in items if item["id"] != expense_id]

        if len(updated_items) == len(items):
            raise ValueError("Expense not found")

        self._write_items(updated_items)

    def clear(self) -> None:
        self._write_items([])

    def _read_items(self) -> List[Dict[str, Any]]:
        data: Dict[str, Any] = self.file_accessor.read()
        return data.get("items", [])

    def _write_items(self, items: List[Dict[str, Any]]) -> None:
        self.file_accessor.write({"items": items})

    def _generate_id(self, items: List[Dict[str, Any]]) -> int:
        if not items:
            return 1

        last_id: int = max(item["id"] for item in items)
        return last_id + 1
