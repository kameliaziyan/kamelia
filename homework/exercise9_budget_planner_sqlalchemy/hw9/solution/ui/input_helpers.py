from solution.ui.http_client import safe_get

KEY_ID = "id"
KEY_DATA = "data"
KEY_KIND = "kind"
CANCEL_OPTION = "0"


def _choose_account() -> str | None:
    response = safe_get("/accounts")

    if not response:
        print("Failed to retrieve accounts. ")
        return None

    accounts = response.get(KEY_DATA, [])

    if not accounts:
        print("No accounts available. ")
        return None

    print("\nAvailable Accounts: ")

    for account in accounts:
        print(
            f"ID: {account['id']}  "
            f"{account['name']}  "
            f"Balance: {account['balance']}",
        )

    valid_ids = set()
    for item in accounts:
        valid_ids.add(str(item[KEY_ID]))

    while True:

        account_id = input("\nEnter account ID (0 to cancel): ").strip()

        if account_id == CANCEL_OPTION:
            return None

        if account_id not in valid_ids:
            print("Invalid account ID. Choose an existing ID. ")
            continue
        return account_id


def _choose_category() -> str | None:

    response = safe_get("/categories")

    if not response:
        print("Failed to retrieve categories. ")
        return None

    categories = response.get(KEY_DATA, [])

    if not categories:
        print("No categories available. ")
        return None

    print("\nAvailable categories: ")

    for category in categories:
        print(
            f"ID: {category['id']}  "
            f"{category['name']}  "
            f"Type: {category['type']}",
        )

    valid_ids = set()
    for item in categories:
        valid_ids.add(str(item[KEY_ID]))

    while True:

        category_id = input("\nEnter category ID (0 to cancel): ").strip()

        if category_id == CANCEL_OPTION:
            return None

        if category_id not in valid_ids:
            print("Invalid category ID. Choose an existing ID. ")
            continue

        return category_id
