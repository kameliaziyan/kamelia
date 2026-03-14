from solution.models.account import Account
from solution.repository.category_repository import CategoryRepository
from solution.repository.account_repository import AccountRepository
from solution.models.transaction import Transaction
from solution.repository.transaction_repository import TransactionRepository
from solution.repository.transfer_repository import TransferRepository
from solution.database.database import async_session_maker
from sqlalchemy.ext.asyncio import AsyncSession


KEY_DATE = "date"


class TransactionService:

    def __init__(self) -> None:
        self._transaction_repository = TransactionRepository()
        self._account_repository = AccountRepository()
        self._category_repository = CategoryRepository()
        self._transfer_repository = TransferRepository()
        self._session_maker = async_session_maker

    async def transactions(self) -> list[Transaction]:
        async with self._session_maker() as session:

            transactions = await self._transaction_repository.get_all(session)
            accounts = {}
            for account in await self._account_repository.get_all(session):
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

    async def add(self, transaction: Transaction) -> Transaction:
        async with self._session_maker() as session:
            async with session.begin():
                self._validate_amount(transaction)
                await self._validate_account(session, transaction.account_id)
                await self._validate_category(session, transaction.category_id)
                return await self._transaction_repository.create(session, transaction)

    async def get(self, transaction_id: int) -> Transaction:
        async with self._session_maker() as session:
            return await self._transaction_repository.get(session, transaction_id)

    async def remove(self, transaction_id: int) -> None:
        async with self._session_maker() as session:
            async with session.begin():
                transaction = await self._transaction_repository.get(
                    session, transaction_id
                )

                transaction.is_deleted = True
                await self._transaction_repository.update(session, transaction)

    async def transaction_history(self) -> list[dict]:
        async with self._session_maker() as session:
            accounts: dict[int, Account]
            accounts = {}
            for account in await self._account_repository.get_all(session):
                if not account.is_deleted:
                    accounts[account.id] = account

            result: list[dict] = []

            for transaction in await self.transactions():
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
            transfers = await self._transfer_repository.get_all(session)

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

    async def _validate_account(self, session: AsyncSession, account_id: int) -> None:
        account = await self._account_repository.get(session, account_id)

        if account is None or account.is_deleted:
            raise ValueError("Account not found.")

    async def _validate_category(self, session: AsyncSession, category_id: int) -> None:
        category = await self._category_repository.get(session, category_id)

        if category is None or category.is_deleted:
            raise ValueError("Category not found.")
