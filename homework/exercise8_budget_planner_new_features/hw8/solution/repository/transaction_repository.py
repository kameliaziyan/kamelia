from hw8.solution.models.transaction import Transaction
from hw8.solution.repository.base_repository import BaseRepository
from hw8.solution.repository.csv_accessor import CsvFileAccessor


class TransactionRepository(BaseRepository[Transaction]):
    def __init__(self) -> None:
        accessor = CsvFileAccessor("data/transactions.csv")
        super().__init__(accessor, Transaction)
