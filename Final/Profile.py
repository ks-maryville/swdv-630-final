from typing import Optional

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from Final.User import User
from Final.db import DB, engine


class Base(DeclarativeBase):
    pass


class Profile(Base, DB):
    __tablename__ = "profile"

    profile_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.user_id))
    first_name: Mapped[str]
    middle_name: Mapped[Optional[str]]
    last_name: Mapped[str] = mapped_column(nullable=False)
    profile_type: Mapped[str]
    # __mapper_args__ = {
    #     "polymorphic_on": "profile_type",
    #     "polymorphic_identity": "profile"
    # }

    def __init__(self, profile_id, user_id, first_name, middle_name, last_name, profile_type):
        self.profile_id = profile_id
        self.user_id = user_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.profile_type = profile_type

    def __repr__(self):
        return f"(\nprofile_id: {self.profile_id}\nuser_id: {self.user_id}\nfirst_name: {self.first_name}\nmiddle_name: {self.middle_name}\nlast_name: {self.last_name}\nprofile_type: {self.profile_type})"


# class WriterProfile(Profile):
#     __mapper_args__ = {
#         "polymorphic_identity": "writer_profile"
#     }


# Base.metadata.drop_all(bind=engine)

Base.metadata.create_all(bind=engine)
