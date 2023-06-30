from sqlalchemy import Column, String, Integer
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from Final.db import *


class User(Base):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True,nullable=False)
    password: Mapped[str]
    role: Mapped[str]

    def __init__(self, user_id, email, password, role):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return f"(\nuser_id: {self.user_id}\nemail: {self.email}\nrole: {self.role}\npassword: {self.password})"
