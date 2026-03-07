from typing import Generic, List, Type, TypeVar

from hw8.solution.repository.csv_accessor import CsvFileAccessor

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
                return self.model_type(**row)

        raise ValueError("Item not found")

    def get_all(self) -> List[ModelT]:
        rows = self.accessor.read()
        return [self.model_type(**row) for row in rows]

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
