from solution.models.account import Account
from solution.repository.base_repository import BaseRepository


class AccountRepository(BaseRepository[Account]):
    def __init__(self) -> None:
        super().__init__(Account)
