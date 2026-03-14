from solution.ui.helper_functions import wait_for_back
from solution.ui.http_client import safe_delete, safe_get, safe_post

KEY_DATA = "data"
KEY_MESSAGE = "message"

CANCEL_OPTION = "0"


def categories_menu() -> None:

    while True:
        choice = input(
            "\n ====== CATEGORIES ======\n"
            "1. View Categories\n"
            "2. Add Category\n"
            "3. Remove Category\n"
            "0. Back\n\n"
            "Choose an option: "
        ).strip()

        if choice == CANCEL_OPTION:
            return

        match choice:
            case "1":
                _view_categories_action()
            case "2":
                _add_category_action()
            case "3":
                _remove_category_action()
            case _:
                print("Invalid option. Please try again.")


def _view_categories_action() -> None:

    response = safe_get("/categories")

    if not response:
        print("Failed to retrieve categories.")
        return

    categories = response[KEY_DATA]

    if not categories:
        print("No categories found.")
        return

    print("\n Current Categories:")

    for category in categories:
        print(
            f"ID: {category['id']}   "
            f"{category['name']}    "
            f"Type: {category['type']}"
        )

    wait_for_back()


def _add_category_action() -> None:

    name = input("Enter category name:  ").strip()

    while True:
        category_type = input("Enter category type (income/expense): ").strip().lower()

        if category_type not in ("income", "expense"):
            print("Invalid type. Use 'income' or 'expense'.")
            continue
        break

    payload = {
        "name": name,
        "type": category_type,
    }

    response = safe_post("/categories", payload)

    if not response:
        return
    print(response.get(KEY_MESSAGE, "Category created."))

    wait_for_back()


def _remove_category_action() -> None:

    response = safe_get("/categories")
    if not response:
        print("Failed to retrieve categories. ")
        wait_for_back()
        return

    categories = response.get(KEY_DATA, [])

    if not categories:
        print("No categories available. ")
        wait_for_back()
        return

    print("\n Current Categories: ")
    for category in categories:
        print(
            f"ID: {category['id']}   "
            f"{category['name']}    "
            f"Type: {category['type']}"
        )

    valid_ids = set()
    for item in categories:
        valid_ids.add(str(item["id"]))

    while True:
        category_id = input("\nEnter category ID to remove (0 to cancel): ").strip()

        if category_id == CANCEL_OPTION:
            return

        if category_id not in valid_ids:
            print("Category not found. Choose an existing ID or 0 to go back. ")
            continue

        response = safe_delete(f"/categories/{category_id}")

        if not response:
            print("Operation failed. ")
            continue

        print(response.get(KEY_MESSAGE, "Category removed."))

        wait_for_back()
        return
