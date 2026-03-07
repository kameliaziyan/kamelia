from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class Transaction:
    id: int
    amount: Decimal
    date: date
    account_id: int
    category_id: int
    is_deleted: bool = False
