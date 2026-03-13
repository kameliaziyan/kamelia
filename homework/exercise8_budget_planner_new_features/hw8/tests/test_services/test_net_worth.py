from decimal import Decimal
from unittest.mock import Mock, patch

from solution.models.account import Account
from solution.services.account_services import AccountService


def test_net_worth_calculation() -> None:
    service = AccountService()
    service._account_repository = Mock()

    accounts = [
        Account(id=1, name="bank1", opening_balance=Decimal("2000")),
        Account(id=2, name="bank2", opening_balance=Decimal("4000")),
        Account(id=3, name="bank3", opening_balance=Decimal("-3000")),
    ]
    service._account_repository.get_all.return_value = accounts
    service._account_repository.get.side_effect = accounts

    with patch.object(service, "_transaction_balance", return_value=Decimal("0")):
        result = service.net_worth
    assert result == Decimal("3000")
