from decimal import Decimal
from unittest.mock import Mock
from solution.models.account import Account
import pytest
from solution.repository.base_repository import BaseRepository


def test_create_account() -> None:
    accessor = Mock()
    accessor.read.return_value = []
    repository = BaseRepository(accessor, Account)

    account = Account(
        id=0,
        name="account1",
        opening_balance=Decimal("4000"),
        is_deleted=False,
    )

    result = repository.create(account)
    assert result.id == 1
    assert result.name == "account1"


def test_get_existing_account() -> None:
    accessor = Mock()

    accessor.read.return_value = [
        {
            "id": "1",
            "name": "account1",
            "opening_balance": "4000",
            "is_deleted": "False",
        }
    ]
    repository = BaseRepository(accessor, Account)
    result = repository.get(1)

    assert result.id == 1
    assert result.name == "account1"


def test_get_all_accounts() -> None:
    accessor = Mock()

    accessor.read.return_value = [
        {
            "id": "1",
            "name": "account1",
            "opening_balance": "4000",
            "is_deleted": "False",
        },
        {
            "id": "2",
            "name": "account2",
            "opening_balance": "2000",
            "is_deleted": "False",
        },
    ]
    repository = BaseRepository(accessor, Account)
    result = repository.get_all()

    assert len(result) == 2
    assert result[0].name == "account1"
    assert result[1].name == "account2"


def test_update_account() -> None:
    accessor = Mock()

    accessor.read.return_value = [
        {
            "id": "1",
            "name": "account1",
            "opening_balance": "4000",
            "is_deleted": "False",
        }
    ]
    repository = BaseRepository(accessor, Account)
    update_account = Account(
        id=1,
        name="new_account",
        opening_balance=Decimal("4000"),
        is_deleted=False,
    )

    result = repository.update(update_account)

    assert result.name == "new_account"


def test_delete_account() -> None:
    accessor = Mock()

    accessor.read.return_value = [
        {
            "id": "1",
            "name": "account1",
            "opening_balance": "4000",
            "is_deleted": "False",
        },
        {
            "id": "2",
            "name": "account2",
            "opening_balance": "2000",
            "is_deleted": "False",
        },
    ]
    repository = BaseRepository(accessor, Account)
    repository.delete(1)
    accessor.write.assert_called_once()
