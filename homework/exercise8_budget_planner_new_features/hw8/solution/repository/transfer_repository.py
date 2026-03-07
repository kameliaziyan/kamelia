from hw8.solution.models.transfer import Transfer
from hw8.solution.repository.base_repository import BaseRepository
from hw8.solution.repository.csv_accessor import CsvFileAccessor


class TransferRepository(BaseRepository[Transfer]):
    def __init__(self) -> None:
        accessor = CsvFileAccessor("data/transfers.csv")
        super().__init__(accessor, Transfer)
