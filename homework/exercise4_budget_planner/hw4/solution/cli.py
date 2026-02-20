from solution.budget import Budget

LINE_WIDTH = 40


class CLI:
    """interface class for the Budget Planner application ."""

    def __init__(self) -> None:
        """Initialize the CLI and create a Budget instance ."""

        self.budget = Budget()

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
        """Process the user's menu selection ."""

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
                self.budget.clear_all()
                print("Your Budget is clear !!")
            case _:
                print("Invalid option. Please try again.")

        return True

    def _view_summary_action(self) -> None:
        """Display a formatted summary of incomes, expenses, and remaining budget."""

        line = "=" * LINE_WIDTH
        separator = "-" * LINE_WIDTH

        summary = self.budget.summary()

        print(f"\n{line}")
        print("        BUDGET SUMMARY")
        print(line)

        self._print_section(
            title="INCOME SOURCES:",
            items=self.budget.incomes,
            total_label="TOTAL INCOME:",
            total_value=summary["total_income"],
            separator=separator,
        )

        self._print_section(
            title="EXPENSES:",
            items=self.budget.expenses,
            total_label="TOTAL EXPENSES:",
            total_value=summary["total_expense"],
            separator=separator,
        )

        remaining = summary["remaining_budget"]
        formatted_remaining = f"${remaining:,.2f}"

        print(f"\n{line}")
        print(f"REMAINING BUDGET:             {formatted_remaining}")
        print(f"{line}\n")

    def _print_section(
        self,
        title: str,
        items: list,
        total_label: str,
        total_value: float,
        separator: str,
    ) -> None:
        """Print a formatted section of income or expense entries."""

        print(f"\n{title}")

        if items:
            for index, item in enumerate(items, start=1):
                description = f"{item.description:<25}"
                amount = f"${item.amount:,.2f}"
                print(f"  {index}. {description} {amount}")
        else:
            print("  No items added.")

        formatted_total = f"${total_value:,.2f}"
        print(separator)
        print(f"{total_label:<30} {formatted_total}")

    def _float_amount(self, message: str) -> float:
        """Convert user input to a float value."""
        return float(input(message))

    def _add_income_action(self) -> None:
        """Handle adding a new income entry from user input."""

        description = input("Enter income description: ").strip()

        while True:
            user_input = input("Enter income amount: ").strip()

            try:
                amount = float(user_input)
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            try:
                self.budget.add(description, amount, "income")
            except ValueError:
                print("Income amount cannot be negative or 0")
                continue

            print("Income added successfully!")
            break

    def _add_expense_action(self) -> None:
        """Handle adding a new expense entry from user  input."""

        description = input("Enter expense description: ").strip()

        while True:

            user_input = input("Enter expense amount: ").strip()

            try:
                amount = float(user_input)
            except ValueError:
                print("Invalid amount.  Please enter a number.")
                continue

            try:
                self.budget.add(description, amount, "expense")
            except ValueError:
                print("Expense amount cannot be negative or 0")
                continue

            print("Expense added successfully!")
            break

    def _remove_income_action(self) -> None:
        """Handle removing an income entry by ID."""

        if not self.budget.incomes:
            print("No incomes to remove.")
            return

        print("\nCurrent Incomes:")
        for income in self.budget.incomes:
            print(
                f"ID: {income.id}    "
                f"{income.description}      "
                f"${income.amount:,.2f}",
            )

        while True:
            user_input = input("Enter income ID to remove: ").strip()

            try:
                item_id = int(user_input)
            except ValueError:
                print("Invalid ID. Please enter a number.")
                continue

            try:
                self.budget.remove(item_id, "income")
            except ValueError:
                print("Income not found. Please try again.")
                continue

            print("Income removed successfully!")
            break

    def _remove_expense_action(self) -> None:
        """Handle removing an expense entry by ID."""

        if not self.budget.expenses:
            print("No expenses to remove.")
            return

        print("\nCurrent Expenses:")
        for expense in self.budget.expenses:
            print(
                f"ID: {expense.id} | "
                f"{expense.description} | "
                f"${expense.amount:,.2f}",
            )

        while True:
            user_input = input("Enter expense ID to remove: ").strip()

            try:
                item_id = int(user_input)
            except ValueError:
                print("Invalid ID. Please enter a number.")
                continue

            try:
                self.budget.remove(item_id, "expense")
            except ValueError:
                print("Expense not found. Please try again.")
                continue

            print("Expense removed successfully!")
            break
