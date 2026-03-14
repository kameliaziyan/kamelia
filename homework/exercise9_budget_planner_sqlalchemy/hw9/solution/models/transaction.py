# from dataclasses import dataclass
# from datetime import date
# from decimal import Decimal


# @dataclass
# class Transaction:#
#    id: int
#    amount: Decimal
#    date: date
#    account_id: int
#    category_id: int
#    is_deleted: bool = False


from datetime import datetime
from decimal import Decimal

from sqlalchemy import Boolean, Date, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from solution.database.database import Base

MAX_NAME_LENGTH = 256


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    amount: Mapped[Decimal] = mapped_column(Numeric(8, 2), nullable=False)
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="CASCADE"), nullable=False
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)

    account = relationship("Account", back_populates="transactions")
    category = relationship("Category", back_populates="transactions")
