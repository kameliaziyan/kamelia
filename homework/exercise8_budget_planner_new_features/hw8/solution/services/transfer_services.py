from solution.models.transfer import Transfer
from solution.repository.transfer_repository import TransferRepository


class TransferService:

    def __init__(self) -> None:
        self._transfer_repository = TransferRepository()

    @property
    def transfers(self) -> list[Transfer]:
        transfers = self._transfer_repository.get_all()
        return [transfer for transfer in transfers if not transfer.is_deleted]

    def add(self, transfer: Transfer) -> Transfer:
        if transfer.amount <= 0:
            raise ValueError("Amount cannot be negative or zero")

        if transfer.from_account_id == transfer.to_account_id:
            raise ValueError("Cannot transfer to the same account")

        return self._transfer_repository.create(transfer)

    def get(self, transfer_id: int) -> Transfer:
        return self._transfer_repository.get(transfer_id)

    def remove(self, transfer_id: int) -> None:
        transfer = self._transfer_repository.get(transfer_id)

        transfer.is_deleted = True
        self._transfer_repository.update(transfer)
