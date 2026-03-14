from enum import Enum
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import Boolean, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from solution.database.database import Base

MAX_NAME_LENGTH = 256

class CategoryType(Enum):
    INCOME = "income"
    EXPENSE = "expense"

    
class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(MAX_NAME_LENGTH), nullable=False)
    type: Mapped[CategoryType] = mapped_column(SQLEnum(CategoryType), nullable=False)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    transactions = relationship(
        "Transaction", back_populates="category", cascade="all, delete-orphan"
    )
