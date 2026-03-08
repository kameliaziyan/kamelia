from solution.models.transaction import Transaction
from solution.repository.transaction_repository import TransactionRepository


class TransactionService:

    def __init__(self) -> None:
        self._transaction_repository = TransactionRepository()

    @property
    def transactions(self) -> list[Transaction]:
        transactions = self._transaction_repository.get_all()
        return [
            transaction for transaction in transactions if not transaction.is_deleted
        ]

    def add(self, transaction: Transaction) -> Transaction:
        if transaction.amount <= 0:
            raise ValueError("Amount cannot be negative or zero")

        return self._transaction_repository.create(transaction)

    def get(self, transaction_id: int) -> Transaction:
        return self._transaction_repository.get(transaction_id)

    def remove(self, transaction_id: int) -> None:
        transaction = self._transaction_repository.get(transaction_id)

        transaction.is_deleted = True
        self._transaction_repository.update(transaction)
