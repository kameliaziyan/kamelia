import requests

STATUS_OK = 200

BASE_URL = "http://localhost:8000"

CONNECTION_ERROR = "Cannot connect to server."
INCOME_ERROR = "Income amount cannot be negative or 0"
EXPENSE_ERROR = "Expense amount cannot be negative or 0"
INCOME_NOT_FOUND = "Income  not found."
EXPENSE_NOT_FOUND = "Expense  not found."
CLEAR_ERROR = "Failed to clear data."
SUMMARY_ERROR = "Failed to retrieve summary."


# python3 solution/budget_planner_ui.py


class UI:

    def actions(self) -> None:
        """Display the interactive menu and process user actions."""
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
                "Choose an option:"
            ).strip()

            if not self._process_action(choice):
                break

    def _process_action(self, data: str) -> bool:
        """Process the user's menu selection."""
        if data == "7":
            return False

        match data:
            case "1":
                self._handle_add_income()
            case "2":
                self._handle_add_expense()
            case "3":
                self._handle_view_summary()
            case "4":
                self._handle_remove_income()
            case "5":
                self._handle_remove_expense()
            case "6":
                self._handle_clear_all()
                print("Your Budget is clear !!")
            case _:
                print("Invalid option. Please try again.")

        return True

    def _handle_add_income(self) -> None:
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
                    params={
                        "description": description,
                        "amount": amount,
                    },
                    timeout=5,
                )
            except requests.exceptions.ConnectionError:
                print(CONNECTION_ERROR)
                return

            if response.status_code != STATUS_OK:
                print(INCOME_ERROR)
                continue

            print("Income added successfully!")
            break

    def _handle_add_expense(self) -> None:
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
                    params={
                        "description": description,
                        "amount": amount,
                    },
                    timeout=5,
                )
            except requests.exceptions.ConnectionError:
                print(CONNECTION_ERROR)
                return

            if response.status_code != STATUS_OK:
                print(EXPENSE_ERROR)
                continue

            print("Expense added successfully!")
            break

    def _safe_get(self, endpoint: str) -> requests.Response | None:
        try:
            response = requests.get(f"{BASE_URL}{endpoint}", timeout=5)
        except requests.exceptions.ConnectionError:
            self._print_connection_error()
            return None

        if response.status_code != STATUS_OK:
            return None

        return response

    def _print_connection_error(self) -> None:
        print(CONNECTION_ERROR)

    def _handle_remove_income(self) -> None:
        response = self._safe_get("/income")
        if response is None:
            print("Failed to retrieve incomes.")
            return

        incomes = response.json()

        if not incomes:
            print("No incomes to remove.")
            return

        print("\nCurrent Incomes:")
        for income in incomes:
            print(
                f"ID: {income['id']}  -"
                f"{income['description']}  "
                f"{income['amount']}",
            )

        user_input = input("Enter income ID to remove: ").strip()

        try:
            item_id = int(user_input)
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        try:
            delete_response = requests.delete(
                f"{BASE_URL}/income/{item_id}",
                timeout=5,
            )
        except requests.exceptions.ConnectionError:
            self._print_connection_error()
            return

        if delete_response.status_code != STATUS_OK:
            print("Income ID not found.")
            return

        print("Income deleted successfully!")

    def _handle_remove_expense(self) -> None:
        response = self._safe_get("/expense")
        if response is None:
            print("Failed to retrieve expenses.")
            return

        expenses = response.json()

        if not expenses:
            print("No expenses to remove.")
            return

        print("\nCurrent Expenses:")
        for expense in expenses:
            print(
                f"ID: {expense['id']}  "
                f"{expense['description']}  "
                f"{expense['amount']}",
            )

        user_input = input("Enter expense ID to remove: ").strip()

        try:
            item_id = int(user_input)
        except ValueError:
            print("Invalid ID. Please enter a number ID .")
            return

        try:
            delete_response = requests.delete(
                f"{BASE_URL}/expense/{item_id}",
                timeout=5,
            )
        except requests.exceptions.ConnectionError:
            self._print_connection_error()
            return

        if delete_response.status_code != STATUS_OK:
            print("Expense ID not found.")
            return

        print("Expense deleted successfully!")

    def _handle_clear_all(self) -> None:
        while True:
            try:
                response = requests.delete(f"{BASE_URL}/clear")
            except requests.exceptions.ConnectionError:
                print(CONNECTION_ERROR)
                continue

            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                print(CLEAR_ERROR)
                continue

            print("All data cleared successfully!")
            break

    def _handle_view_summary(self) -> None:
        while True:
            try:
                response = requests.get(f"{BASE_URL}/summary")
            except requests.exceptions.ConnectionError:
                print(CONNECTION_ERROR)
                continue

            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                print(SUMMARY_ERROR)
                continue

            return_values = response.json()

            #initial print to check the code.fix it!!!!
            print("\n----- Budget Summary -----")
            print(f"Total Income: {return_values['total_income']}")
            print(f"Total Expense: {return_values['total_expense']}")
            print(f"Remaining Budget: {return_values['remaining_budget']}")
            print("--------------------------\n")

            break


if __name__ == "__main__":
    ui = UI()
    ui.actions()
