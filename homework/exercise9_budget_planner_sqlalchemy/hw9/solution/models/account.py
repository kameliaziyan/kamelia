# from dataclasses import dataclass
# from decimal import Decimal


# @dataclass
# class Account:
#    id: int
#    name: str
#    opening_balance: Decimal
#    is_deleted: bool = False

from decimal import Decimal

from sqlalchemy import Boolean, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from solution.database.database import Base

MAX_NAME_LENGTH = 256


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(MAX_NAME_LENGTH), nullable=False)
    opening_balance: Mapped[Decimal] = mapped_column(Numeric(8, 2), nullable=False)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    transactions = relationship(
        "Transaction", back_populates="account", cascade="all, delete-orphan"
    )
    out_transfers = relationship(
        "Transfer",
        foreign_keys="Transfer.from_account_id",
        back_populates="from_account",
        cascade="all, delete-orphan",
    )
    in_transfers = relationship(
        "Transfer",
        foreign_keys="Transfer.to_account_id",
        back_populates="to_account",
        cascade="all, delete-orphan",
    )
