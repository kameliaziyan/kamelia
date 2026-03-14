from solution.models.category import Category
from solution.repository.category_repository import CategoryRepository
from solution.database.database import async_session_maker


class CategoryService:

    def __init__(self) -> None:
        self._category_repository = CategoryRepository()
        self._session_maker = async_session_maker

    async def categories(self) -> list[Category]:
        async with self._session_maker() as session:

            return await self._category_repository.get_all(session)

    async def add(self, category: Category) -> Category:
        async with self._session_maker() as session:
            async with session.begin():

                return await self._category_repository.create(session, category)

    async def get(self, category_id: int) -> Category:
        async with self._session_maker() as session:

            return await self._category_repository.get(session, category_id)

    async def remove(self, category_id: int) -> None:
        async with self._session_maker() as session:
            async with session.begin():

                await self._category_repository.delete(session, category_id)
