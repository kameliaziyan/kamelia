from solution.models.transaction import Transaction
from solution.repository.base_repository import BaseRepository


class TransactionRepository(BaseRepository[Transaction]):
    def __init__(self) -> None:
        super().__init__(Transaction)
