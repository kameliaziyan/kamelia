from solution.models.transfer import Transfer
from solution.repository.base_repository import BaseRepository


class TransferRepository(BaseRepository[Transfer]):
    def __init__(self) -> None:
        super().__init__(Transfer)
