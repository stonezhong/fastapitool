from typing import List
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Student(Base):
    __tablename__ = "students"

    id:                     Mapped[int] = mapped_column(Integer, primary_key=True)
    name:                   Mapped[str] = mapped_column(String(128))
    age:                    Mapped[int] = mapped_column(Integer)
