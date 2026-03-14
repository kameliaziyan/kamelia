import asyncio
from decimal import Decimal

from solution.models.account import Account
from solution.models.category import CategoryType
from solution.repository.account_repository import AccountRepository
from solution.repository.category_repository import CategoryRepository
from solution.repository.transaction_repository import TransactionRepository
from solution.repository.transfer_repository import TransferRepository
from solution.database.database import async_session_maker
from sqlalchemy.ext.asyncio import AsyncSession



class AccountService:

    def __init__(self) -> None:
        self._account_repository = AccountRepository()
        self._transaction_repository = TransactionRepository()
        self._transfer_repository = TransferRepository()
        self._category_repository = CategoryRepository()
        self._session_maker = async_session_maker

    async def accounts(self) -> list[Account]:
        async with self._session_maker() as session:

            accounts = await self._account_repository.get_all(session)
            active_accounts: list[Account] = []
            for account in accounts:
                if account.is_deleted is False:
                    active_accounts.append(account)
            return active_accounts

    async def net_worth(self) -> Decimal:
        accounts = await self.accounts()
        balances = await asyncio.gather(*(self.balance(account.id) for account in accounts))

        result = sum(balances, Decimal("0"))
        return result

    async def add(self, account: Account) -> Account:
        async with self._session_maker() as session:
            async with session.begin():

                return await self._account_repository.create(session, account)

    async def get(self, account_id: int) -> Account:
        async with self._session_maker() as session:

            return await self._account_repository.get(session, account_id)

    async def balance(self, account_id: int) -> Decimal:
        async with self._session_maker() as session:

            account = await self._account_repository.get(session, account_id)
            balance = account.opening_balance
            balance += await self._transaction_balance(session, account_id)
            balance += await self._transfer_balance(session, account_id)

            return balance

    async def remove(self, account_id: int) -> None:
        async with self._session_maker() as session:
            async with session.begin():
                account = await self._account_repository.get(session, account_id)
                account.is_deleted = True

                await self._account_repository.update(session, account)

    async def _transaction_balance(self, session: AsyncSession, account_id: int) -> Decimal:
        balance = Decimal("0")

        transactions = await self._transaction_repository.get_all(session)
        categories = {}
        for current_category in await self._category_repository.get_all(session):
            categories[current_category.id] = current_category

        for transaction in transactions:
            if transaction.account_id != account_id or transaction.is_deleted:
                continue

            transaction_category = categories[transaction.category_id]

            if transaction_category.type == CategoryType.INCOME:
                balance += transaction.amount
            else:
                balance -= transaction.amount

        return balance

    async def _transfer_balance(self, session: AsyncSession, account_id: int) -> Decimal:
        balance = Decimal("0")

        transfers = await self._transfer_repository.get_all(session)

        for transfer in transfers:
            if transfer.is_deleted:
                continue

            if transfer.to_account_id == account_id:
                balance += transfer.amount

            if transfer.from_account_id == account_id:
                balance -= transfer.amount

        return balance
