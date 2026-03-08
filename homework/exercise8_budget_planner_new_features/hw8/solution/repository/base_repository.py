from datetime import date
from decimal import Decimal
from typing import Generic, List, Type, TypeVar

from solution.repository.csv_accessor import CsvFileAccessor

ModelT = TypeVar("ModelT")
ID = "id"


class BaseRepository(Generic[ModelT]):

    def __init__(self, accessor: CsvFileAccessor, model_type: Type[ModelT]) -> None:
        self.accessor = accessor
        self.model_type = model_type

    def create(self, item: ModelT) -> ModelT:
        rows = self.accessor.read()

        if rows:
            new_id = max(int(row[ID]) for row in rows) + 1
        else:
            new_id = 1

        item_dict = vars(item)
        item_dict[ID] = new_id
        rows.append(item_dict)
        self.accessor.write(rows)

        return self.model_type(**item_dict)

    def get(self, item_id: int) -> ModelT:

        rows = self.accessor.read()

        for row in rows:
            if int(row[ID]) == item_id:
                row = self._convert_types(row)
                return self.model_type(**row)

        raise ValueError("Item not found")

    def get_all(self) -> List[ModelT]:
        rows = self.accessor.read()
        return [self.model_type(**self._convert_types(row)) for row in rows]

    def delete(self, item_id: int) -> None:
        rows = self.accessor.read()
        rows = [row for row in rows if int(row[ID]) != item_id]
        self.accessor.write(rows)

    def update(self, item: ModelT) -> ModelT:
        rows = self.accessor.read()

        item_id = vars(item)[ID]

        for result, row in enumerate(rows):
            if int(row[ID]) == item_id:
                rows[result] = vars(item)

        self.accessor.write(rows)
        return item

    def _convert_types(self, row: dict) -> dict:
        result = row.copy()

        identifier = result.get(ID)
        if identifier is not None:
            result[ID] = int(identifier)

        opening_balance = result.get("opening_balance")
        if opening_balance is not None:
            result["opening_balance"] = Decimal(opening_balance)

        amount = result.get("amount")
        if amount is not None:
            result["amount"] = Decimal(amount)

        is_deleted = result.get("is_deleted")
        if is_deleted is not None:
            result["is_deleted"] = is_deleted == "True"

        date = result.get("date")
        if date is not None:
            result["date"] = date.fromisoformat(date)

        return result
