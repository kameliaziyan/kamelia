from datetime import date
from decimal import Decimal
from typing import Dict, Generic, List, Type, TypeVar, Callable
from solution.models.category import CategoryType
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
        items: list[ModelT] = []
        for row in rows:
            converted_row = self._convert_types(row)
            items.append(self.model_type(**converted_row))
        return items

    def delete(self, item_id: int) -> None:
        rows = self.accessor.read()
        filterd_rows = []
        item_found = False
        for row in rows:
            if int(row[ID]) == item_id:
                item_found = True
                continue
            filterd_rows.append(row)

        if not item_found:
            raise ValueError("Item not found")
        self.accessor.write(filterd_rows)

    def update(self, item: ModelT) -> ModelT:
        rows = self.accessor.read()

        item_id = vars(item)[ID]

        for result, row in enumerate(rows):
            if int(row[ID]) == item_id:
                rows[result] = vars(item)
                self.accessor.write(rows)
                return item
        raise ValueError("Item not found.")

    def _convert_types(self, row: dict) -> dict:
        result = row.copy()
        self._apply_converters(
            result,
            {
                ID: int,
                "account_id": int,
                "category_id": int,
                "from_account_id": int,
                "to_account_id": int,
                "opening_balance": Decimal,
                "amount": Decimal,
                "date": date.fromisoformat,
                "type": self._convert_category_type,
            },
        )
        self._convert_bool_field(result, "is_deleted")
        return result

    def _apply_converters(
        self,
        row: dict,
        converters: Dict[str, Callable[[str], object]],
    ) -> None:
        for field, converter in converters.items():
            value = row.get(field)
            if value is not None:
                row[field] = converter(value)

    def _convert_bool_field(self, row: dict, field: str) -> None:
        value = row.get(field)
        if value is not None:
            row[field] = value == "True"

    def _convert_category_type(self, value: str) -> CategoryType:
        if "CategoryType." in value:
            value = value.split(".")[1].lower()
        return CategoryType(value)
