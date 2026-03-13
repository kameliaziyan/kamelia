from decimal import Decimal

from solution.models.transaction import Transaction
from solution.models.category import CategoryType
from solution.services.category_services import CategoryService
from solution.services.transaction_services import TransactionService


class ReportService:
    def __init__(self) -> None:
        self._transaction_service = TransactionService()
        self._category_service = CategoryService()

    def spending_by_category(self, year: int, month: int) -> dict[str, Decimal]:
        transactions = self._transaction_service.transactions
        categories_by_id = self._get_categories_by_id()
        result: dict[str, Decimal] = {}

        for transaction in transactions:
            if not self._is_in_requested_month(transaction, year, month):
                continue

            current_category = categories_by_id.get(transaction.category_id)
            if current_category is None:
                continue

            if current_category.type != CategoryType.EXPENSE:
                continue

            category_name = current_category.name
            current_amount = result.get(category_name, Decimal("0"))
            result[category_name] = current_amount + transaction.amount
        return result

    def monthly_summary(self, year: int, month: int) -> dict[str, Decimal]:
        transactions = self._transaction_service.transactions
        categories_by_id = self._get_categories_by_id()

        income = Decimal("0")
        expenses = Decimal("0")

        for transation in transactions:
            if not self._is_in_requested_month(transation, year, month):
                continue

            current_category = categories_by_id.get(transation.category_id)
            if current_category is None:
                continue

            if current_category.type == CategoryType.INCOME:
                income += transation.amount
            elif current_category.type == CategoryType.EXPENSE:
                expenses += transation.amount

        return {
            "income": income,
            "expenses": expenses,
            "net_cash_flow": income - expenses,
        }

    def _get_categories_by_id(self) -> dict:
        categories_by_id = {}
        for category in self._category_service.categories:
            categories_by_id[category.id] = category

        return categories_by_id

    def _is_in_requested_month(
        self, transaction: Transaction, year: int, month: int
    ) -> bool:
        return transaction.date.year == year and transaction.date.month == month
