from datetime import date
from decimal import Decimal
from unittest.mock import Mock

from solution.models.category import Category, CategoryType
from solution.models.transaction import Transaction
from solution.services.report_services import ReportService


def test_monthly_summary_calculation() -> None:
    service = ReportService()
    service._transaction_service = Mock()
    service._category_service = Mock()

    service._transaction_service.transactions = [
        Transaction(
            id=1,
            account_id=1,
            category_id=2,
            amount=Decimal("200"),
            date=date(2026, 3, 11),
        ),
        Transaction(
            id=2,
            account_id=1,
            category_id=2,
            amount=Decimal("200"),
            date=date(2026, 3, 13),
        ),
        Transaction(
            id=3,
            account_id=1,
            category_id=2,
            amount=Decimal("100"),
            date=date(2026, 3, 11),
        ),
    ]

    service._category_service.categories = [
        Category(
            id=1,
            name="salary",
            type=CategoryType.INCOME,
        ),
        Category(
            id=2,
            name="food",
            type=CategoryType.EXPENSE,
        ),
    ]
    result = service.monthly_summary(2026, 3)

    assert result["income"] == Decimal("0")
    assert result["expenses"] == Decimal("500")
    assert result["net_cash_flow"] == Decimal("-500")
