from datetime import date

from solution.ui.input_helpers import _choose_account
from solution.ui.helper_functions import (
    _get_account_names,
    _get_transfer_account_name,
    wait_for_back,
)
from solution.ui.http_client import safe_delete, safe_get, safe_post

KEY_DATA = "data"
KEY_MESSAGE = "message"

CANCEL_OPTION = "0"


def transfers_menu() -> None:
    while True:
        choice = input(
            "\n ====== TRANSFERS ======\n"
            "1. View Transfers\n"
            "2. Add Transfer\n"
            "3. Remove Transfer\n"
            "0. Back\n\n"
            "Choose an option:  "
        ).strip()

        if choice == CANCEL_OPTION:
            return

        match choice:
            case "1":
                _view_transfers_action()
            case "2":
                _add_transfer_action()
            case "3":
                _remove_transfer_action()
            case _:
                print("Invalid option. Please try again.")


def _view_transfers_action() -> None:

    response = safe_get("/transfers")

    if not response:
        print("Failed to retrieve transfers.")
        wait_for_back()
        return

    transfers = response.get(KEY_DATA, [])

    if not transfers:
        print("No transfers found.")
        wait_for_back()
        return
    account_names = _get_account_names()

    print("\nCurrent Transfers: ")

    for transfer in transfers:
        from_name = _get_transfer_account_name(
            transfer["from_account_id"], account_names
        )
        to_name = _get_transfer_account_name(transfer["to_account_id"], account_names)

        print(
            f"ID: {transfer['id']}   "
            f"From: {from_name}   "
            f"To: {to_name}   "
            f"Amount:  ${transfer['amount']}   "
            f"Date: {transfer['date']}"
        )
    wait_for_back()


def _add_transfer_action() -> None:

    amount = input("Enter transfer amount: ").strip()
    from_account = _choose_account()
    if not from_account:
        return
    to_account = _choose_account()
    if not to_account:
        return

    if from_account == to_account:
        print("Source and destination accounts cannot be the same.")

    today = str(date.today())

    payload = {
        "amount": amount,
        "from_account_id": from_account,
        "to_account_id": to_account,
        "date": today,
    }

    response = safe_post("/transfers", payload)

    if not response:
        return

    print(response.get(KEY_MESSAGE, "Transfer created."))


def _remove_transfer_action() -> None:

    response = safe_get("/transfers")
    if not response:
        print("Failed to retrieve transfers. ")
        wait_for_back()
        return

    transfers = response.get(KEY_DATA, [])

    if not transfers:
        print("No transfers available. ")
        wait_for_back()
        return

    print("/Current transfers: ")
    for transfer in transfers:
        print(
            f"ID: {transfer['id']}   "
            f"From: {transfer['from_account_id']}    "
            f"To: {transfer['to_account_id']}  "
            f"Amount: ${transfer['amount']}",
        )

    valid_ids = set()
    for item in transfers:
        valid_ids.add(str(item["id"]))

    while True:
        transfer_id = input("\nEnter transfer ID to remove (0 to cancel): ").strip()

        if transfer_id == CANCEL_OPTION:
            return

        if transfer_id not in valid_ids:
            print("Transfers not found. Choose an existing ID or 0 to go back. ")
            continue

        response = safe_delete(f"/transfers/{transfer_id}")

        if not response:
            print("Operation failed. ")
            continue

        print(response.get(KEY_MESSAGE, "Transfers removed."))

        wait_for_back()
        return
