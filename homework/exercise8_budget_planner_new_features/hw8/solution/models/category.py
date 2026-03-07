from dataclasses import dataclass
from enum import Enum


class CategoryType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


@dataclass
class Category:
    id: int
    name: str
    type: CategoryType
