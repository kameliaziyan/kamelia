import requests

LINE_WIDTH = 40
STATUS_OK = 200
BASE_URL = "http://localhost:8000"

CONNECTION_ERROR = "Cannot connect to server."


class UI:
    """Interface class for the Budget Planner application via HTTP."""

    def actions(self) -> None:
        while True:
            choice = input(
                "===== BUDGET PLANNER =====\n"
                "1. Add Income\n"
                "2. Add Expense\n"
                "3. View Summary\n"
                "4. Remove Income\n"
                "5. Remove Expense\n"
                "6. Clear All Data\n"
                "7. Exit\n\n"
                "Choose an option: "
            ).strip()

            if not self._process_action(choice):
                break

    def _process_action(self, data: str) -> bool:
        if data == "7":
            return False

        match data:
            case "1":
                self._add_income_action()
            case "2":
                self._add_expense_action()
            case "3":
                self._view_summary_action()
            case "4":
                self._remove_income_action()
            case "5":
                self._remove_expense_action()
            case "6":
                self._clear_all_action()
            case _:
                print("Invalid option. Please try again.")

        return True

    def _add_income_action(self) -> None:
        description = input("Enter income description: ").strip()

        while True:
            try:
                amount = float(input("Enter income amount: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            try:
                response = requests.post(
                    f"{BASE_URL}/income",
                    json={"description": description, "amount": amount},
                )
            except requests.exceptions.ConnectionError:
                print(CONNECTION_ERROR)
                return

            if response.status_code == STATUS_OK:
                print("Income added successfully!")
                break
            else:
                print("Operation failed.")
                continue

    def _add_expense_action(self) -> None:
        description = input("Enter expense description: ").strip()

        while True:
            try:
                amount = float(input("Enter expense amount: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            try:
                response = requests.post(
                    f"{BASE_URL}/expense",
                    json={"description": description, "amount": amount},
                )
            except requests.exceptions.ConnectionError:
                print(CONNECTION_ERROR)
                return

            if response.status_code == STATUS_OK:
                print("Expense added successfully!")
                break
            else:
                print("Operation failed.")
                continue

    def _view_summary_action(self) -> None:
        try:
            response = requests.get(f"{BASE_URL}/summary")
        except requests.exceptions.ConnectionError:
            print(CONNECTION_ERROR)
            return

        if response.status_code != STATUS_OK:
            print("Failed to retrieve summary.")
            return

        response_data = response.json()

        summary = response_data["data"]

        line = "=" * LINE_WIDTH
        separator = "-" * LINE_WIDTH

        print(f"\n{line}")
        print("        BUDGET SUMMARY")
        print(line)

        print(separator)
        print(f"TOTAL INCOME:                 ${summary['total_income']:,.2f}")
        print(f"TOTAL EXPENSE:                ${summary['total_expense']:,.2f}")
        print(separator)
        print(f"REMAINING BUDGET:             ${summary['remaining_budget']:,.2f}")
        print(f"{line}\n")

    def _remove_income_action(self) -> None:
        try:
            response = requests.get(f"{BASE_URL}/income")
        except requests.exceptions.ConnectionError:
            print(CONNECTION_ERROR)
            return

        if response.status_code != STATUS_OK:
            print("Failed to retrieve incomes.")
            return

        response_data = response.json()
        incomes = response_data["data"]

        if not incomes:
            print("No incomes to remove.")
            return

        print("\nCurrent Incomes:")
        for income in incomes:
            print(
                f"ID: {income['id']}  "
                f"{income['description']}  "
                f"${income['amount']:,.2f}",
            )

        try:
            item_id = int(input("Enter income ID to remove: "))
        except ValueError:
            print("Invalid ID.")
            return

        delete_response = requests.delete(
            f"{BASE_URL}/income/{item_id}",
        )

        if delete_response.status_code != STATUS_OK:
            print("Income not found.")
            return

        print("Income removed successfully!")

    def _remove_expense_action(self) -> None:
        try:
            response = requests.get(f"{BASE_URL}/expense")
        except requests.exceptions.ConnectionError:
            print(CONNECTION_ERROR)
            return

        if response.status_code != STATUS_OK:
            print("Failed to retrieve expenses.")
            return

        response_data = response.json()
        expenses = response_data["data"]

        if not expenses:
            print("No expenses to remove.")
            return

        print("\nCurrent Expenses:")
        for expense in expenses:
            print(
                f"ID: {expense['id']}  "
                f"{expense['description']}  "
                f"${expense['amount']:,.2f}",
            )

        try:
            item_id = int(input("Enter expense ID to remove: "))
        except ValueError:
            print("Invalid ID.")
            return

        delete_response = requests.delete(
            f"{BASE_URL}/expense/{item_id}",
        )

        if delete_response.status_code != STATUS_OK:
            print("Expense not found.")
            return

        print("Expense removed successfully!")

    def _clear_all_action(self) -> None:
        try:
            response = requests.delete(f"{BASE_URL}/clear")
        except requests.exceptions.ConnectionError:
            print(CONNECTION_ERROR)
            return

        if response.status_code != STATUS_OK:
            print("Failed to clear data.")
            return

        print("All data cleared successfully!")



