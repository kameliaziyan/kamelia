from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class Transfer:
    id: int
    from_account_id: int
    to_account_id: int
    amount: Decimal
    date: date
    is_deleted: bool = False
