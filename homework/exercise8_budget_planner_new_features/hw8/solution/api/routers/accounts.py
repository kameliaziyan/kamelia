from dataclasses import dataclass
from decimal import Decimal

from solution.models.account import Account
from solution.services.account_services import AccountService
from fastapi import APIRouter

KEY_MESSAGE = "message"
KEY_DATA = "data"
KEY_DETAILS = "details"
KEY_ID = "id"
KEY_NAME = "name"
KEY_BALANCE = "balance"
KEY_OPENING_BALANCE = "opening_balance"
KEY_NET_WORTH = "net_worth"

router = APIRouter()
account_service = AccountService()


@dataclass
class AccountRequest:
    name: str
    opening_balance: Decimal


@router.post("/accounts")
async def create_account(account_data: AccountRequest) -> dict:

    account = Account(
        id=0,
        name=account_data.name,
        opening_balance=account_data.opening_balance,
    )

    created_account = account_service.add(account)

    return {
        KEY_MESSAGE: "Account created successfully",
        KEY_DETAILS: {
            KEY_ID: created_account.id,
            KEY_NAME: created_account.name,
            KEY_OPENING_BALANCE: str(created_account.opening_balance),
        },
    }


@router.get("/accounts")
async def list_accounts() -> dict:

    accounts = account_service.accounts

    return {
        KEY_MESSAGE: "Accounts retrieved",
        KEY_DATA: [
            {
                KEY_ID: account.id,
                KEY_NAME: account.name,
                KEY_BALANCE: str(account_service.balance(account.id)),
            }
            for account in accounts
        ],
    }


@router.delete("/accounts/{account_id}")
async def remove_account(account_id: int) -> dict:

    account_service.remove(account_id)
    return {KEY_MESSAGE: "Account removed successfully"}


@router.get("/accounts/{account_id}/balance")
async def get_balance(account_id: int) -> dict:

    balance = account_service.balance(account_id)

    return {
        KEY_MESSAGE: "Account balance retrieved",
        KEY_DATA: {KEY_BALANCE: str(balance)},
    }


@router.get("/net-worth")
async def get_net_worth() -> dict:

    net_worth = account_service.net_worth

    return {
        KEY_MESSAGE: "Net worth retrieved",
        KEY_DATA: {KEY_NET_WORTH: str(net_worth)},
    }
