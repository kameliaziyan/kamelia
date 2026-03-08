from solution.models.category import Category
from solution.repository.base_repository import BaseRepository
from solution.repository.csv_accessor import CsvFileAccessor


class CategoryRepository(BaseRepository[Category]):
    def __init__(self) -> None:
        accessor = CsvFileAccessor("data/categories.csv")
        super().__init__(accessor, Category)
