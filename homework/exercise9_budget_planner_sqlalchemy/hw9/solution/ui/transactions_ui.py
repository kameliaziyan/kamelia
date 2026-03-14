from datetime import date
from solution.ui.input_helpers import _choose_account, _choose_category
from solution.ui.helper_functions import _format_transaction_row
from solution.ui.helper_functions import _get_account_names, _get_category_names
from solution.ui.helper_functions import wait_for_back
from solution.ui.http_client import safe_delete, safe_get, safe_post

KEY_DATA = "data"
KEY_MESSAGE = "message"
KEY_ID = "id"
CANCEL_OPTION = "0"


def transactions_menu() -> None:

    while True:
        choice = input(
            "\n ====== TRANSACTIONS ======\n"
            "1. View Transactions\n"
            "2. Add Income Transations\n"
            "3. Add Expense Transation\n"
            "4. Remove Transation\n"
            "0. Back\n\n"
            "Choose an option: "
        ).strip()

        if choice == CANCEL_OPTION:
            return

        match choice:
            case "1":
                _view_transactions_action()
            case "2":
                _add_transaction_action("income")
            case "3":
                _add_transaction_action("expense")
            case "4":
                _remove_transaction_action()
            case _:
                print("Invalid option. Please try again.")


def _view_transactions_action() -> None:
    response = safe_get("/transaction-history")

    if not response:
        print("Faild to retrieve transations.")
        wait_for_back()
        return

    transactions = response.get(KEY_DATA, [])

    if not transactions:
        print("No transactions found.")
        wait_for_back()
        return

    account_names = _get_account_names()
    category_names = _get_category_names()

    print("\n{}".format("=" * 100))
    header = "{:<18}{:<18}{:<20}{:<22}{:<14}{:<14}".format(
        "ID", "TYPE", "ACCOUNT", "INFO", "AMOUNT", "DATE"
    )
    print(header)
    print("-" * 100)
    for item in transactions:
        print(_format_transaction_row(item, account_names, category_names))
    print("=" * 100)

    wait_for_back()


def _add_transaction_action(transaction_type: str) -> None:

    amount = input("Enter amount: ").strip()
    account_id = _choose_account()
    if not account_id:
        return

    category_id = _choose_category()
    if not category_id:
        return

    today = str(date.today())

    payload = {
        "amount": amount,
        "account_id": account_id,
        "category_id": category_id,
        "date": today,
    }

    response = safe_post("/transactions", payload)

    if not response:
        print("Operation failed.")
        return

    print(response.get(KEY_MESSAGE, "Transaction created."))

    wait_for_back()


def _remove_transaction_action() -> None:

    response = safe_get("/transactions")
    if not response:
        print("Failed to retrieve transactions. ")
        wait_for_back()
        return

    transactions = response.get(KEY_DATA, [])

    if not transactions:
        print("No transactions available. ")
        wait_for_back()
        return

    print("/Current transactions: ")
    for transaction in transactions:
        print(
            f"ID: {transaction['id']}   "
            f"Amount: {transaction['amount']}    "
            f"Account: {transaction['account_id']}  "
            f"Category: {transaction['category_id']}",
        )

    valid_ids = set()
    for item in transactions:
        valid_ids.add(str(item[KEY_ID]))

    while True:
        transaction_id = input(
            "\nEnter transaction ID to remove (0 to cancel): "
        ).strip()

        if transaction_id == CANCEL_OPTION:
            return

        if transaction_id not in valid_ids:
            print("Transaction not found. Choose an existing ID or 0 to go back. ")
            continue

        response = safe_delete(f"/transactions/{transaction_id}")

        if not response:
            print("Operation failed. ")
            continue

        print(response.get(KEY_MESSAGE, "Transaction removed."))

        wait_for_back()
        return
