from solution.budget import Budget


class CLI:
    def __init__(self) -> None:
        self.budget = Budget()

    def actions(self) -> None:
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
        if data == "7":
            return False

        match data:
            case "1":
                self._handle_add_income()
            case "2":
                self._handle_add_expense()
            case "3":
                print( self._handle_view_summary())
            case "4":
                self._handle_remove_income()
            case "5":
                self._handle_remove_expense()
            case "6":
                self.budget.clear_all()
                print("Clear Budget !!")
            case _:
                print("Invalid option. Please try again.")

        return True
    
    def _handle_view_summary(self) -> None:
        incomes = self.budget.get_incomes()
        expenses = self.budget.get_expenses()

        print("\n" + "=" * 40)
        print("        BUDGET SUMMARY")
        print("=" * 40)

        # Income section
        print("\nINCOME SOURCES:")
        if incomes:
            for index, income in enumerate(incomes, start=1):
                print(f"  {index}. {income.description:<20} ${income.amount:,.2f}")
        else:
            print("  No income sources added.")

        print("-" * 40)
        print(f"TOTAL INCOME:           ${self.budget.total_income():,.2f}")

        # Expense section
        print("\nEXPENSES:")
        if expenses:
            for index, expense in enumerate(expenses, start=1):
                print(f"  {index}. {expense.description:<20} ${expense.amount:,.2f}")
        else:
            print("  No expenses added.")

        print("-" * 40)
        print(f"TOTAL EXPENSES:         ${self.budget.total_expense():,.2f}")

        print("\n" + "=" * 40)
        print(f"REMAINING BUDGET:       ${self.budget.remaining_budget():,.2f}")
        print("=" * 40 + "\n")


    def _float_amount(self, message: str) -> float:
        return float(input(message))

    def _handle_add_income(self) -> None:
        description = input("Enter income description: ")
        # if not description:
        #    print("Operation cancelled.")
        #    return

        while True:
            try:
                amount = self._float_amount("Enter income amount: ")
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
                continue

            self.budget.add_income(description, amount)
            print("Income added successfully!")
            break

    def _handle_add_expense(self) -> None:
        description = input("Enter expense description: ")

        while True:
            try:
                amount = self._float_amount("Enter expense amount: ")
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
                continue

            self.budget.add_expense(description, amount)
            print("Expense added successfully!")
            break

    def _handle_remove_income(self) -> None:
        while True:
            description = input("Enter income description to remove: ")
            try:
                self.budget.remove_income(description)

            except ValueError:
                print("Income not found. Please try again.")
                continue

            print("Income removed successfully!")
            break

    def _handle_remove_expense(self) -> None:

        while True:
            description = input("Enter expense description to remove: ")
            try:
                self.budget.remove_expense(description)

            except ValueError:
                print("Expense not found. Please try again.")
                continue

            print("Expense removed successfully!")
            break
