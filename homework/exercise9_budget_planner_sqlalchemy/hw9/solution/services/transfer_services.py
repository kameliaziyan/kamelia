from solution.models.transfer import Transfer
from solution.repository.transfer_repository import TransferRepository
from solution.repository.account_repository import AccountRepository
from solution.models.account import Account
from solution.database.database import async_session_maker
from sqlalchemy.ext.asyncio import AsyncSession


class TransferService:

    def __init__(self) -> None:
        self._transfer_repository = TransferRepository()
        self._account_repository = AccountRepository()
        self._session_maker = async_session_maker

    async def transfers(self) -> list[Transfer]:
        async with self._session_maker() as session:

            transfers = await self._transfer_repository.get_all(session)
            accounts = await self._get_active_accounts(session)
            valid_transfers: list[Transfer] = []
            for transfer in transfers:
                if not self._is_visible_transfer(transfer, accounts):
                    continue
                valid_transfers.append(transfer)

            return valid_transfers

    async def add(self, transfer: Transfer) -> Transfer:
        if transfer.amount <= 0:
            raise ValueError("Amount cannot be negative or zero")

        if transfer.from_account_id == transfer.to_account_id:
            raise ValueError("Cannot transfer to the same account")

        async with self._session_maker() as session:
            async with session.begin():

                from_account = await self._account_repository.get(
                    session, transfer.from_account_id
                )
                to_account = await self._account_repository.get(
                    session, transfer.to_account_id
                )

                if from_account.is_deleted or to_account.is_deleted:
                    raise ValueError("Account not found")

                return await self._transfer_repository.create(session, transfer)

    async def get(self, transfer_id: int) -> Transfer:
        async with self._session_maker() as session:
            return await self._transfer_repository.get(session, transfer_id)

    async def remove(self, transfer_id: int) -> None:
        async with self._session_maker() as session:
            async with session.begin():
                transfer = await self._transfer_repository.get(session, transfer_id)

                transfer.is_deleted = True
                await self._transfer_repository.update(session, transfer)

    async def _get_active_accounts(self, session: AsyncSession) -> dict:
        accounts: dict[int, Account]
        accounts = {}

        for account in await self._account_repository.get_all(session):
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
