from hw8.solution.models.category import Category
from hw8.solution.repository.category_repository import CategoryRepository


class CategoryService:

    def __init__(self) -> None:
        self._category_repository = CategoryRepository()

    @property
    def categories(self) -> list[Category]:
        return self._category_repository.get_all()

    def add(self, category: Category) -> Category:

        return self._category_repository.create(category)

    def get(self, category_id: int) -> Category:
        return self._category_repository.get(category_id)

    def remove(self, category_id: int) -> None:

        self._category_repository.delete(category_id)
