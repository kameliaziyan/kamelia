from solution.ui.helper_functions import wait_for_back
from solution.ui.http_client import safe_get

LINE_WIDTH = 40
KEY_DATA = "data"
CANCEL_OPTION = "0"


def reports_menu() -> None:

    while True:
        choice = input(
            "\n ====== REPORTS ======\n"
            "1. Monthly Summary\n"
            "2. Spending by Category\n"
            "0. Back\n\n"
            "Choose an option: "
        ).strip()

        if choice == CANCEL_OPTION:
            return

        match choice:
            case "1":
                _monthly_summary_action()
            case "2":
                _spending_by_category_action()
            case _:
                print("Invalid option. Please try again.")


def _monthly_summary_action() -> None:

    year = input("Enter year (YYYY): ").strip()
    month = input("Enter month (MM): ").strip()

    response = safe_get(f"/summary?year={year}&month={month}")

    if not response:
        print("Faild to retrieve summary. ")
        return

    summary = response[KEY_DATA]

    line = "=" * LINE_WIDTH
    separator = "-" * LINE_WIDTH

    print(f"\n{line}")
    print("           MONTHLY SUMMARY")
    print(line)

    print(f"Total Income:         ${summary['income']}")
    print(f"Total Expenses:         ${summary['expenses']}")

    print(separator)
    print(f"Net Cash Flow:         ${summary['net_cash_flow']}")

    print(f"{line}\n")
    wait_for_back()


def _spending_by_category_action() -> None:

    year = input("Enter year (YYYY): ").strip()
    month = input("Enter month (MM): ").strip()

    response = safe_get(f"/spending-by-category?year={year}&month={month}")

    if not response:
        print("Faild to retrieve spending data. ")
        return

    data = response[KEY_DATA]

    if not data:
        print("No spending data found.")
        return

    line = "=" * LINE_WIDTH

    print(f"\n{line}")
    print(".      SPENDING BY CATEGORY")
    print(line)

    for category, amount in data.items():
        print(f"{category:<25}   ${amount}")

    print(f"{line}\n")
    wait_for_back()
