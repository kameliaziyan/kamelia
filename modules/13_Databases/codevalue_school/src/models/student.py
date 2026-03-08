import datetime

from sqlalchemy import Date, DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

MAX_EMAIL_LENGTH = 255
MAX_NAME_LENGTH = 100


# Exxercise 1: Define the Student model here
class Student(Base):
    __tablename__ = "students"


    student_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    birth_date: Mapped[Date] = mapped_column(Date, nullable= True)
    created_at: Mapped[DateTime] = mapped_column(DateTime)

