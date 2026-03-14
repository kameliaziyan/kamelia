from dataclasses import dataclass
from decimal import Decimal
from datetime import date
from fastapi import APIRouter

from solution.models.transfer import Transfer
from solution.services.transfer_services import TransferService

KEY_MESSAGE = "message"
KEY_DATA = "data"
KEY_DETAILS = "details"
KEY_ID = "id"
KEY_AMOUNT = "amount"
KEY_FROM = "from_account_id"
KEY_TO = "to_account_id"
KEY_DATE = "date"

router = APIRouter()
transfer_service = TransferService()


@dataclass
class TransferRequest:
    amount: Decimal
    from_account_id: int
    to_account_id: int
    date: date


@router.post("/transfers")
async def create_transfer(transfer_data: TransferRequest) -> dict:

    transfer = Transfer(
        id=0,
        amount=transfer_data.amount,
        from_account_id=transfer_data.from_account_id,
        to_account_id=transfer_data.to_account_id,
        date=transfer_data.date,
    )

    created_transfer = await transfer_service.add(transfer)

    return {
        KEY_MESSAGE: "Transfer created successfully",
        KEY_DETAILS: {
            KEY_ID: created_transfer.id,
            KEY_AMOUNT: str(created_transfer.amount),
            KEY_FROM: created_transfer.from_account_id,
            KEY_TO: created_transfer.to_account_id,
            KEY_DATE: str(created_transfer.date),
        },
    }


@router.get("/transfers")
async def list_transfers() -> dict:

    transfers = await transfer_service.transfers()

    return {
        KEY_MESSAGE: "transfers retrieved",
        KEY_DATA: [
            {
                KEY_ID: transfer.id,
                KEY_AMOUNT: str(transfer.amount),
                KEY_FROM: transfer.from_account_id,
                KEY_TO: transfer.to_account_id,
                KEY_DATE: str(transfer.date),
            }
            for transfer in transfers
        ],
    }


@router.delete("/transfers/{transfer_id}")
async def remove_transfer(transfer_id: int) -> dict:

    await transfer_service.remove(transfer_id)
    return {KEY_MESSAGE: "Transfers removed successfully"}
