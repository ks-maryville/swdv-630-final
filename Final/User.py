from sqlalchemy import Column, String, Integer
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    _id = Column("_id", Integer, primary_key=True)
    email = Column("email", String, unique=True, nullable=False)
    password = Column("password", String, nullable=False)
    role = Column("role", String, nullable=False)

    def __init__(self, _id, email, password, role):
        self._id = _id
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return f"({self._id}\n{self.email}\n{self.role})"
