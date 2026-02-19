import requests

BASE_URL = "http://localhost:8000"

CONNECTION_ERROR = "Cannot connect to server. Is the API running?"
INCOME_ERROR = "Income amount cannot be negative or 0"
EXPENSE_ERROR = "Expense amount cannot be negative or 0"
INCOME_NOT_FOUND = "Income description not found."
EXPENSE_NOT_FOUND = "Expense description not found."
CLEAR_ERROR = "Failed to clear data."
SUMMARY_ERROR = "Failed to retrieve summary."


# python3 solution/budget_planner_ui.py


class UI:

    def actions(self) -> None:
        """Display the interactive menu and process user actions."""
        while True:
            data = input(
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

            if not self._process_action(data):
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
        while True:
            description = input("Enter income description: ").strip()

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
                )
            except requests.exceptions.ConnectionError:
                print(CONNECTION_ERROR)
                continue

            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                print(INCOME_ERROR)
                continue

            print("Income added successfully!")
            break

    def _handle_add_expense(self) -> None:
        while True:
            description = input("Enter expense description: ").strip()

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
                )
            except requests.exceptions.ConnectionError:
                print(CONNECTION_ERROR)
                continue

            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                print(EXPENSE_ERROR)
                continue

            print("Expense added successfully!")
            break

    def _handle_remove_income(self) -> None:
        while True:
            description = input("Enter income description: ").strip()

            try:
                response = requests.delete(f"{BASE_URL}/income_/{description}")
            except requests.exceptions.ConnectionError:
                print(CONNECTION_ERROR)
                continue

            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                print(INCOME_NOT_FOUND)
                continue

            print("Income deleted successfully!")
            break

    def _handle_remove_expense(self) -> None:
        while True:
            description = input("Enter expense description: ").strip()

            try:
                response = requests.delete(f"{BASE_URL}/expense_/{description}")
            except requests.exceptions.ConnectionError:
                print(CONNECTION_ERROR)
                continue

            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                print(EXPENSE_NOT_FOUND)
                continue

            print("Expense deleted successfully!")
            break

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

            data = response.json()

            print("\n----- Budget Summary -----")
            print(f"Total Income: {data['total_income']}")
            print(f"Total Expense: {data['total_expense']}")
            print(f"Remaining Budget: {data['remaining_budget']}")
            print("--------------------------\n")

            break


if __name__ == "__main__":
    ui = UI()
    ui.actions()
