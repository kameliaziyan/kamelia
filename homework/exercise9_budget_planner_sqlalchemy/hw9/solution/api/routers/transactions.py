from dataclasses import dataclass
from decimal import Decimal
from datetime import date
from fastapi import APIRouter

from solution.models.transaction import Transaction
from solution.services.transaction_services import TransactionService

KEY_MESSAGE = "message"
KEY_DATA = "data"
KEY_DETAILS = "details"
KEY_ID = "id"
KEY_AMOUNT = "amount"
KEY_ACCOUNT = "account_id"
KEY_CATEGORY = "category_id"
KEY_DATE = "date"

router = APIRouter()
transaction_service = TransactionService()


@dataclass
class TransactionRequest:
    amount: Decimal
    account_id: int
    category_id: int
    date: date


@router.post("/transactions")
async def create_transaction(transaction_data: TransactionRequest) -> dict:

    transaction = Transaction(
        id=0,
        amount=transaction_data.amount,
        account_id=transaction_data.account_id,
        category_id=transaction_data.category_id,
        date=transaction_data.date,
    )

    try:
        created_transaction = await transaction_service.add(transaction)
    except ValueError as error:
        return {KEY_MESSAGE: str(error)}

    return {
        KEY_MESSAGE: "Transaction created successfully",
        KEY_DETAILS: {
            KEY_ID: created_transaction.id,
            KEY_AMOUNT: str(created_transaction.amount),
            KEY_ACCOUNT: created_transaction.account_id,
            KEY_CATEGORY: created_transaction.category_id,
            KEY_DATE: str(created_transaction.date),
        },
    }


@router.get("/transactions")
async def list_transactions() -> dict:

    transactions = await transaction_service.transactions()

    return {
        KEY_MESSAGE: "transactions retrieved",
        KEY_DATA: [
            {
                KEY_ID: transaction.id,
                KEY_AMOUNT: str(transaction.amount),
                KEY_ACCOUNT: transaction.account_id,
                KEY_CATEGORY: transaction.category_id,
                KEY_DATE: str(transaction.date),
            }
            for transaction in transactions
        ],
    }


@router.delete("/transactions/{transaction_id}")
async def remove_transaction(transaction_id: int) -> dict:

    await transaction_service.remove(transaction_id)
    return {KEY_MESSAGE: "Transaction removed successfully"}


@router.get("/transaction-history")
async def list_transaction_history() -> dict:
    history = await transaction_service.transaction_history()
    return {
        KEY_MESSAGE: "Transaction history retrieved",
        KEY_DATA: history,
    }
