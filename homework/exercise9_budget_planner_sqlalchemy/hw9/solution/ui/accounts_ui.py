from solution.ui.helper_functions import wait_for_back
from solution.ui.http_client import safe_delete, safe_get, safe_post

KEY_DATA = "data"
KEY_MESSAGE = "message"
KEY_PATH_ACCOUNTS = "/accounts"
CANCEL_OPTION = "0"


def accounts_menu() -> None:
    while True:
        choice = input(
            "\n====== ACCOUNTS ======\n"
            "1. View Accounts\n"
            "2. Add Account\n"
            "3. Remove Account\n"
            "4. View Account Balance\n"
            "5. View Net Worth\n"
            "0. Back\n\n"
            "Choose an option: "
        ).strip()

        if choice == CANCEL_OPTION:
            return

        match choice:

            case "1":
                _view_accounts_action()
            case "2":
                _add_account_action()
            case "3":
                _remove_account_action()
            case "4":
                _view_balance_action()
            case "5":
                _view_net_worth_action()

            case _:
                print("Invalid option. Please try again. ")


def _view_accounts_action() -> None:

    response = safe_get(KEY_PATH_ACCOUNTS)

    if not response:
        print("Faild to retrieve accounts. ")
        return

    accounts = response[KEY_DATA]

    if not accounts:
        print("No accounts found. ")
        return

    print("\n Current Accounts: ")

    for account in accounts:
        print(
            f"ID: {account['id']}  "
            f"{account['name']}    "
            f"Balance: ${account['balance']}"
        )

    wait_for_back()


def _add_account_action() -> None:

    name = input("Enter account name:  ").strip()
    opening_balance = input("Enter opening balance:  ").strip()

    payload = {
        "name": name,
        "opening_balance": opening_balance,
    }

    response = safe_post(KEY_PATH_ACCOUNTS, payload)

    if not response:
        return
    print(response.get(KEY_MESSAGE, "Account created."))

    wait_for_back()


def _remove_account_action() -> None:
    response = safe_get(KEY_PATH_ACCOUNTS)
    if not response:
        print("Faild to retrieve accounts.")
        wait_for_back()
        return

    accounts = response.get(KEY_DATA, [])
    if not accounts:
        print("No accounts available.")
        wait_for_back()
        return

    print("\nCurrent Accounts:")
    for account in accounts:
        print(
            f"ID: {account['id']}   "
            f"{account['name']}   "
            f"Balance: ${account['balance']}"
        )

    valid_ids = set()
    for item in accounts:
        valid_ids.add(str(item["id"]))

    while True:
        account_id = input("Enter account ID to remove: ").strip()

        if account_id == CANCEL_OPTION:
            return
        if account_id not in valid_ids:
            print("Account not found. " "Choose an existing ID or 0 to go back. ")
            continue

        response = safe_delete(f"/accounts/{account_id}")
        if not response:
            print("Operation failed.")
            continue

        print(response.get(KEY_MESSAGE, "Account removed."))
        wait_for_back()
        return


def _view_balance_action() -> None:
    response = safe_get(KEY_PATH_ACCOUNTS)
    if not response:
        print("Failed to retrieve accounts.")
        wait_for_back()
        return
    accounts = response.get(KEY_DATA, [])
    if not accounts:
        print("No accounts available.")
        wait_for_back()
        return
    print("\nCurrent Accounts:")
    for account in accounts:
        print(f"ID: {account['id']}  " f"{account['name']}   ")

    valid_ids = set()
    for item in accounts:
        valid_ids.add(str(item["id"]))

    while True:
        account_id = input("\nEnter account ID (0 to cancel): ").strip()
        if account_id == CANCEL_OPTION:
            return
        if account_id not in valid_ids:
            print("Account not found. Choose an existing ID (0 to cancel).")
            continue

        balance_response = safe_get(f"/accounts/{account_id}/balance")
        if not balance_response:
            print("Faild to retrieve balance.")
            wait_for_back()
            return

        balance = balance_response[KEY_DATA]["balance"]
        print(f"\n Account balance: ${balance}")
        wait_for_back()
        return


def _view_net_worth_action() -> None:

    response = safe_get("/net-worth")
    if not response:
        print("Faild to retrieve net worth.")
        return

    net_worth = response[KEY_DATA]["net_worth"]
    print(f"\n Net Worth: ${net_worth}")
    wait_for_back()
