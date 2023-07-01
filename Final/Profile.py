from typing import Optional, List

from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Final.User import User
from Final.db import *


class Profile(Base):
    __tablename__ = "profile"

    profile_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.user_id))
    first_name: Mapped[Optional[str]]
    middle_name: Mapped[Optional[str]]
    last_name: Mapped[Optional[str]]
    profile_type: Mapped[str]

    articles: Mapped[Optional[List["Article"]]] = relationship(back_populates="profile")

    __mapper_args__ = {
        "polymorphic_on": "profile_type",
        "polymorphic_identity": "profile"
    }

    def __init__(self, profile_id, user_id, first_name, middle_name, last_name, profile_type):
        self.profile_id = profile_id
        self.user_id = user_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.profile_type = profile_type
