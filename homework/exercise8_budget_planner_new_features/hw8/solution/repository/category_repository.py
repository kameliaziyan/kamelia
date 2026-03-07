from hw8.solution.models.category import Category
from hw8.solution.repository.base_repository import BaseRepository
from hw8.solution.repository.csv_accessor import CsvFileAccessor


class CategoryRepository(BaseRepository[Category]):
    def __init__(self) -> None:
        accessor = CsvFileAccessor("data/categories.csv")
        super().__init__(accessor, Category)
