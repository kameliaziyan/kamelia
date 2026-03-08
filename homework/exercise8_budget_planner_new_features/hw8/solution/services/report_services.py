from collections import defaultdict
from decimal import Decimal

from solution.models.category import CategoryType
from solution.services.category_services import CategoryService
from solution.services.transaction_services import TransactionService


class ReportService:
    def __init__(self) -> None:
        self._transaction_service = TransactionService()
        self._category_service = CategoryService()

    def spending_by_category(self, year: int, month: int) -> dict[str, Decimal]:
        transactions = self._transaction_service.transactions
        categories = {
                category.id: category for category in self._category_service.categories

        }
        result: dict[str, Decimal] = {}

        for transaction in transactions:
            if transaction.date.year != year or transaction.date.month != month:
                continue

            category = categories[transaction.category_id]

            if category.type != CategoryType.EXPENSE:
                continue

            if category.name not in result:
                result[category.name] = Decimal("0")

            result[category.name] += transaction.amount

        return dict(result)

    def monthly_summary(self, year: int, month: int) -> dict[str, Decimal]:
        transactions = self._transaction_service.transactions
        categories = {
            category.id: category for category in self._category_service.categories
        }

        income = Decimal("0")
        expenses = Decimal("0")

        for transation in transactions:
            if transation.date.year != year or transation.date.month != month:
                continue

            category = categories[transation.category_id]

            if category.type == CategoryType.INCOME:
                income += transation.amount
            else:
                expenses += transation.amount

        return {
            "income": income,
            "expenses": expenses,
            "net_cash_flow": income - expenses,
        }
