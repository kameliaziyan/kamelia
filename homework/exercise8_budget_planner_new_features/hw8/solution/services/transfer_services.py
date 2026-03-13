from solution.models.transfer import Transfer
from solution.repository.transfer_repository import TransferRepository
from solution.repository.account_repository import AccountRepository
from solution.models.account import Account


class TransferService:

    def __init__(self) -> None:
        self._transfer_repository = TransferRepository()
        self._account_repository = AccountRepository()

    @property
    def transfers(self) -> list[Transfer]:
        transfers = self._transfer_repository.get_all()
        accounts = self._get_active_accounts()
        valid_transfers: list[Transfer] = []
        for transfer in transfers:
            if not self._is_visible_transfer(transfer, accounts):
                continue
            valid_transfers.append(transfer)

        return valid_transfers

    def add(self, transfer: Transfer) -> Transfer:
        if transfer.amount <= 0:
            raise ValueError("Amount cannot be negative or zero")

        if transfer.from_account_id == transfer.to_account_id:
            raise ValueError("Cannot transfer to the same account")

        from_account = self._account_repository.get(transfer.from_account_id)
        to_account = self._account_repository.get(transfer.to_account_id)

        if from_account.is_deleted or to_account.is_deleted:
            raise ValueError("Account not found")

        return self._transfer_repository.create(transfer)

    def get(self, transfer_id: int) -> Transfer:
        return self._transfer_repository.get(transfer_id)

    def remove(self, transfer_id: int) -> None:
        transfer = self._transfer_repository.get(transfer_id)

        transfer.is_deleted = True
        self._transfer_repository.update(transfer)

    def _get_active_accounts(self) -> dict:
        accounts: dict[int, Account]
        accounts = {}

        for account in self._account_repository.get_all():
            if not account.is_deleted:
                accounts[account.id] = account
        return accounts

    def _is_visible_transfer(
        self, transfer: Transfer, accounts: dict[int, Account]
    ) -> bool:
        if transfer.is_deleted:
            return False
        if (
            transfer.from_account_id not in accounts
            and transfer.to_account_id not in accounts
        ):
            return False
        return True
