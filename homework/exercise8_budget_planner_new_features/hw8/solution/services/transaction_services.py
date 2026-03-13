from solution.models.account import Account
from solution.repository.category_repository import CategoryRepository
from solution.repository.account_repository import AccountRepository
from solution.models.transaction import Transaction
from solution.repository.transaction_repository import TransactionRepository
from solution.repository.transfer_repository import TransferRepository

KEY_DATE = "date"


class TransactionService:

    def __init__(self) -> None:
        self._transaction_repository = TransactionRepository()
        self._account_repository = AccountRepository()
        self._category_repository = CategoryRepository()
        self._transfer_repository = TransferRepository()

    @property
    def transactions(self) -> list[Transaction]:
        transactions = self._transaction_repository.get_all()
        accounts = {}
        for account in self._account_repository.get_all():
            if not account.is_deleted:
                accounts[account.id] = account

        valid_transactions: list[Transaction] = []
        for transaction in transactions:
            if transaction.is_deleted:
                continue
            if transaction.account_id not in accounts:
                continue
            valid_transactions.append(transaction)

        return valid_transactions

    def add(self, transaction: Transaction) -> Transaction:
        self._validate_amount(transaction)
        self._validate_account(transaction.account_id)
        self._validate_category(transaction.category_id)
        return self._transaction_repository.create(transaction)

    def get(self, transaction_id: int) -> Transaction:
        return self._transaction_repository.get(transaction_id)

    def remove(self, transaction_id: int) -> None:
        transaction = self._transaction_repository.get(transaction_id)

        transaction.is_deleted = True
        self._transaction_repository.update(transaction)

    def transaction_history(self) -> list[dict]:
        accounts: dict[int, Account]
        accounts = {}
        for account in self._account_repository.get_all():
            if not account.is_deleted:
                accounts[account.id] = account

        result: list[dict] = []

        for transaction in self.transactions:
            result.append(
                {
                    "id": transaction.id,
                    "kind": "transaction",
                    "account_id": transaction.account_id,
                    "category_id": transaction.category_id,
                    "amount": str(transaction.amount),
                    KEY_DATE: str(transaction.date),
                }
            )
        transfers = self._transfer_repository.get_all()

        for transfer in transfers:
            if transfer.is_deleted:
                continue
            if transfer.from_account_id in accounts:
                result.append(
                    {
                        "id": f"transfer-out-{transfer.id}",
                        "kind": "transfer_out",
                        "account_id": transfer.from_account_id,
                        "related_account_id": transfer.to_account_id,
                        "category_id": "-",
                        "amount": f"-{transfer.amount}",
                        KEY_DATE: str(transfer.date),
                    }
                )
            if transfer.to_account_id in accounts:

                result.append(
                    {
                        "id": f"transfer-in-{transfer.id}",
                        "kind": "transfer_in",
                        "account_id": transfer.to_account_id,
                        "related_account_id": transfer.from_account_id,
                        "category_id": "-",
                        "amount": str(transfer.amount),
                        KEY_DATE: str(transfer.date),
                    }
                )

        result.sort(key=lambda item: item[KEY_DATE], reverse=True)
        return result

    def _validate_amount(self, transaction: Transaction) -> None:
        if transaction.amount <= 0:
            raise ValueError("Amount cannot be negative or zero.")

    def _validate_account(self, account_id: int) -> None:
        try:
            account = self._account_repository.get(account_id)
        except ValueError as error:
            raise ValueError("Account not found") from error
        if account.is_deleted:
            raise ValueError("Account not found.")

    def _validate_category(self, category_id: int) -> None:
        try:
            self._category_repository.get(category_id)
        except ValueError as error:
            raise ValueError("Category not found.") from error
