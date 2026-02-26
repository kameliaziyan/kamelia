import requests

LINE_WIDTH = 40
STATUS_OK = 200
BASE_URL = "http://localhost:8000"

KEY_DATA = "data"
CANCEL_OPTION = "0"
OPERATION_FAILED = "Operation failed."


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

    def _safe_get(self, endpoint: str) -> dict | None:
        try:
            response = requests.get(f"{BASE_URL}{endpoint}")
        except requests.exceptions.ConnectionError:
            print(CONNECTION_ERROR)
            return None
        if response.status_code != STATUS_OK:
            return None
        return response.json()

    def _print_section(
        self,
        title: str,
        items: list,
        total_label: str,
        total_value: float,
        separator: str,
    ) -> None:
        print(f"\n{title}")

        if items:
            for index, item in enumerate(items, start=1):
                description = f"{item['description']:<25}"
                amount = f"${item['amount']:,.2f}"
                print(f"  {index}. {description} {amount}")
        else:
            print("  No items added.")

        formatted_total = f"${total_value:,.2f}"
        print(separator)
        print(f"{total_label:<30} {formatted_total}")

    def _view_summary_action(self) -> None:
        summary_data = self._safe_get("/summary")
        income_data = self._safe_get("/income")
        expense_data = self._safe_get("/expense")

        if not summary_data or not income_data or not expense_data:
            print("Failed to retrieve summary.")
            return

        summary = summary_data[KEY_DATA]
        incomes = income_data[KEY_DATA]
        expenses = expense_data[KEY_DATA]

        line = "=" * LINE_WIDTH
        separator = "-" * LINE_WIDTH

        print(f"\n{line}")
        print("            BUDGET SUMMARY")
        print(line)

        self._print_section(
            title="INCOME SOURCES:",
            items=incomes,
            total_label="TOTAL INCOME:",
            total_value=summary["total_income"],
            separator=separator,
        )

        self._print_section(
            title="EXPENSES:",
            items=expenses,
            total_label="TOTAL EXPENSES:",
            total_value=summary["total_expense"],
            separator=separator,
        )

        print(f"\n{line}")
        print(
            "REMAINING BUDGET:             " f"${summary['remaining_budget']:,.2f}",
        )
        print(f"{line}\n")

    def _add_income_action(self) -> None:
        description = input("Enter income description: ").strip()

        while True:
            amount_input = input("Enter income amount: ").strip()

            try:
                amount = float(amount_input)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
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
                print("Income added successfully.")
                return

            print(OPERATION_FAILED)

    def _add_expense_action(self) -> None:
        description = input("Enter expense description: ").strip()

        while True:
            amount_input = input("Enter expense amount: ").strip()

            try:
                amount = float(amount_input)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
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
                print("Expense added successfully.")
                return

            print(OPERATION_FAILED)

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
        incomes = response_data[KEY_DATA]

        if not incomes:
            print("No incomes available to remove.")
            return

        print("\nCurrent Incomes:")
        for income in incomes:
            print(
                f"ID: {income['id']}  "
                f"{income['description']}  "
                f"${income['amount']:,.2f}",
            )

        while True:
            try:
                item_id = int(input("Enter income ID to remove: "))
            except ValueError:
                print("Invalid ID. Please enter a valid number.")
                continue

            delete_response = requests.delete(
                f"{BASE_URL}/income/{item_id}",
            )

            if delete_response.status_code != STATUS_OK:
                print(OPERATION_FAILED)
                continue

            message = delete_response.json().get(
                "message",
                "Income removed.",
            )
            print(message)
            if message == "Income removed successfully":
                return

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
        expenses = response_data[KEY_DATA]

        if not expenses:
            print("No expenses available to remove.")
            return

        print("\nCurrent Expenses:")
        for expense in expenses:
            print(
                f"ID: {expense['id']}  "
                f"{expense['description']}  "
                f"${expense['amount']:,.2f}",
            )

        while True:
            try:
                item_id = int(input("Enter expense ID to remove: "))
            except ValueError:
                print("Invalid ID. Please enter a valid number.")
                continue

            delete_response = requests.delete(
                f"{BASE_URL}/expense/{item_id}",
            )

            if delete_response.status_code != STATUS_OK:
                print(OPERATION_FAILED)
                continue

            message = delete_response.json().get(
                "message",
                "Expense removed.",
            )
            print(message)

            if message == "Expense removed successfully":
                return

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
