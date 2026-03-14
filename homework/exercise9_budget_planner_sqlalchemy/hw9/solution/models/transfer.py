# from dataclasses import dataclass
# from datetime import date
# from decimal import Decimal


# @dataclass
# class Transfer:
#    id: int
#    from_account_id: int
#    to_account_id: int
#    amount: Decimal
#    date: date
#    is_deleted: bool = False


from datetime import datetime
from decimal import Decimal

from sqlalchemy import Boolean, Date, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from solution.database.database import Base

MAX_NAME_LENGTH = 256


class Transfer(Base):
    __tablename__ = "transfers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    from_account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False
    )
    to_account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False
    )
    amount: Mapped[Decimal] = mapped_column(Numeric(8, 2), nullable=False)
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)

    from_account = relationship(
        "Account", foreign_keys=[from_account_id], back_populates="out_transfers"
    )
    to_account = relationship(
        "Account", foreign_keys=[to_account_id], back_populates="in_transfers"
    )
