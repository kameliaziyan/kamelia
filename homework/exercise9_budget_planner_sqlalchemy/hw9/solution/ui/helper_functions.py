from solution.ui.http_client import safe_get

KEY_ID = "id"
KEY_DATA = "data"
KEY_KIND = "kind"
CANCEL_OPTION = "0"


def wait_for_back() -> None:
    while True:
        choice = input("\nEnter 0 to go back: ").strip()

        if choice == "0":
            return

        print("Invalid option. Please enter 0.")


def _get_account_names() -> dict:
    response = safe_get("/accounts")
    if not response:
        return {}
    accounts = response.get(KEY_DATA, [])
    account_names: dict[int, str] = {}
    for account in accounts:
        account_names[account[KEY_ID]] = account["name"]

    return account_names


def _get_category_names() -> dict:
    response = safe_get("/categories")
    if not response:
        return {}
    categories = response.get(KEY_DATA, [])
    category_names: dict[int, str] = {}
    for category in categories:
        category_names[category[KEY_ID]] = category["name"]

    return category_names


def _format_transaction_kind(kind: str) -> str:
    if kind == "transaction":
        return "Transaction"
    if kind == "transfer_in":
        return "Transfer In"
    if kind == "transfer_out":
        return "Transfer Out"

    return kind


def _format_transaction_row(
    item: dict, account_names: dict, category_names: dict
) -> str:
    account_name = _get_account_name(item, account_names)
    related_account_name = _get_related_account_name(item, account_names)
    item_type = _format_transaction_kind(item[KEY_KIND])
    if item[KEY_KIND] == "transaction":
        info = f"Category: {_get_category_name(item, category_names)}"
    elif item[KEY_KIND] == "transfer_in":
        info = f"From: {related_account_name}"
    elif item[KEY_KIND] == "transfer_out":
        info = f"To: {related_account_name}"
    else:
        info = "-"

    return "{:<18}{:<18}{:<20}{:<22}${:<13}{:<14}".format(
        str(item["id"]),
        item_type,
        account_name,
        info,
        str(item["amount"]),
        item["date"],
    )


def _get_account_name(item: dict, account_names: dict) -> str:
    account_id = item["account_id"]
    account_name = account_names.get(account_id)
    if account_name is not None:
        return account_name
    return "Deleted account"


def _get_related_account_name(item: dict, account_names: dict) -> str:

    related_account_value = item.get("related_account_id")
    if related_account_value is None:
        return "-"
    account_name = account_names.get(related_account_value)
    if account_name is not None:
        return account_name
    return "Deleted account"


def _get_category_name(item: dict, category_names: dict) -> str:
    category_value = item["category_id"]
    if not isinstance(category_value, int):
        return "-"
    category_name = category_names.get(category_value)
    if category_name is not None:
        return category_name
    return "Deleted category"


def _get_extra_information(item: dict, related_account_name: str) -> str:
    if item[KEY_KIND] == "transfer_out":
        return f"To {related_account_name}   "
    if item[KEY_KIND] == "transfer_in":
        return f"From {related_account_name}   "
    category_name = item.get("category_name")
    if category_name:
        return str(category_name)
    return ""


def _get_transfer_account_name(account_id: int, account_names: dict) -> str:
    account_name = account_names.get(account_id)
    if account_name is not None:
        return account_name
    return "Deleted account"
