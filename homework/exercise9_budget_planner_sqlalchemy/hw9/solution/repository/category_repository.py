from solution.models.category import Category
from solution.repository.base_repository import BaseRepository


class CategoryRepository(BaseRepository[Category]):
    def __init__(self) -> None:
        super().__init__(Category)
