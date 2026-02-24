from dataclasses import asdict
from typing import TYPE_CHECKING, List, Dict, Any, Optional

from solution.repository.file_accessor import JsonFileAccessor

if TYPE_CHECKING:
    from solution.budget_hw4_bonus import Income

DATA_FILE = "data/incomes.json"


class IncomeRepository:
    def __init__(
        self,
        file_accessor: Optional[JsonFileAccessor] = None,
    ) -> None:
        self.file_accessor: JsonFileAccessor = (
            file_accessor if file_accessor else JsonFileAccessor(DATA_FILE)
        )

    def create(self, income: "Income") -> "Income":
        from solution.budget_hw4_bonus import Income

        items = self._read_items()

        income.id = self._generate_id(items)
        items.append(asdict(income))

        self._write_items(items)
        return income

    def get_all(self) -> List["Income"]:
        from solution.budget_hw4_bonus import Income

        items = self._read_items()
        incomes: List[Income] = []

        for item in items:
            incomes.append(Income(**item))

        return incomes

    def delete(self, income_id: int) -> None:
        items = self._read_items()

        updated_items = [item for item in items if item["id"] != income_id]

        if len(updated_items) == len(items):
            raise ValueError("Income not found")

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
