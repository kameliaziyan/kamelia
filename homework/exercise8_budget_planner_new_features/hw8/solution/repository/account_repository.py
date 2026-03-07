from hw8.solution.models.account import Account
from hw8.solution.repository.base_repository import BaseRepository
from hw8.solution.repository.csv_accessor import CsvFileAccessor


class AccountRepository(BaseRepository[Account]):
    def __init__(self) -> None:
        accessor = CsvFileAccessor("data/accounts.csv")
        super().__init__(accessor, Account)
