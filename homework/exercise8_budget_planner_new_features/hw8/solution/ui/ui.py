from solution.ui.accounts_ui import accounts_menu
from solution.ui.categories_ui import categories_menu
from solution.ui.data_ui import export_data, import_data
from solution.ui.reports_ui import reports_menu
from solution.ui.transactions_ui import transactions_menu
from solution.ui.transfers_ui import transfers_menu


class UI:
    def actions(self) -> None:
        while True:
            choice = input(
                "====== BUDGET PLANNER =====\n"
                "1. Accounts\n"
                "2. Categories\n"
                "3. Transactions\n"
                "4. Transfers\n"
                "5. Reports\n"
                "6. Export Data\n"
                "7. Import Data\n"
                "8. Exit\n\n"
                "Choose an option: "
            ).strip()

            if not self._process_action(choice):
                break

    def _process_action(self, choice: str) -> bool:

        if choice == "8":
            return False

        actions = {
            "1": accounts_menu,
            "2": categories_menu,
            "3": transactions_menu,
            "4": transfers_menu,
            "5": reports_menu,
            "6": export_data,
            "7": import_data,
        }
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid option. Please try again.")

        return True
