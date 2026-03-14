from typing import Generic, List, Type, TypeVar
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

ModelT = TypeVar("ModelT")
ID = "id"


class BaseRepository(Generic[ModelT]):

    def __init__(self, model_type: Type[ModelT]) -> None:
        self.model_type = model_type

    async def create(self, session: AsyncSession, item: ModelT) -> ModelT:
        session.add(item)
        await session.flush()
        return item

    async def get(self, session: AsyncSession, item_id: int) -> ModelT:
        result = await session.get(self.model_type, item_id)
        return result

    async def get_all(self, session: AsyncSession) -> List[ModelT]:
        result = await session.scalars(select(self.model_type))
        return list(result)

    async def delete(self, session: AsyncSession, item_id: int) -> None:
        item = await session.get(self.model_type, item_id)
        if item:
            await session.delete(item)
            await session.commit()

    async def update(self, session: AsyncSession, item: ModelT) -> ModelT:
        session.add(item)
        await session.flush()
        return item
