from decimal import Decimal

from solution.models.account import Account
from solution.models.category import CategoryType
from solution.repository.account_repository import AccountRepository
from solution.repository.category_repository import CategoryRepository
from solution.repository.transaction_repository import TransactionRepository
from solution.repository.transfer_repository import TransferRepository


class AccountService:

    def __init__(self) -> None:
        self._account_repository = AccountRepository()
        self._transaction_repository = TransactionRepository()
        self._transfer_repository = TransferRepository()
        self._category_repository = CategoryRepository()

    @property
    def accounts(self) -> list[Account]:
        accounts = self._account_repository.get_all()
        return [account for account in accounts if not account.is_deleted]

    @property
    def net_worth(self) -> Decimal:
        return sum(
            (self.balance(account.id) for account in self.accounts),
            Decimal("0"),
        )

    def add(self, account: Account) -> Account:
        return self._account_repository.create(account)

    def get(self, account_id: int) -> Account:
        return self._account_repository.get(account_id)

    def balance(self, account_id: int) -> Decimal:
        account = self._account_repository.get(account_id)

        balance = account.opening_balance

        balance += self._transaction_balance(account_id)
        balance += self._transfer_balance(account_id)

        return balance

    def remove(self, account_id: int) -> None:
        account = self._account_repository.get(account_id)
        account.is_deleted = True

        self._account_repository.update(account)

    def _transaction_balance(self, account_id: int) -> Decimal:
        balance = Decimal("0")

        transactions = self._transaction_repository.get_all()
        categories = {
            category.id: category for category in self._category_repository.get_all()
        }

        for transaction in transactions:
            if transaction.account_id != account_id or transaction.is_deleted:
                continue

            category = categories[transaction.category_id]

            if category.type == CategoryType.INCOME:
                balance += transaction.amount
            else:
                balance -= transaction.amount

        return balance

    def _transfer_balance(self, account_id: int) -> Decimal:
        balance = Decimal("0")

        transfers = self._transfer_repository.get_all()

        for transfer in transfers:
            if transfer.is_deleted:
                continue

            if transfer.to_account_id == account_id:
                balance += transfer.amount

            if transfer.from_account_id == account_id:
                balance -= transfer.amount

        return balance
