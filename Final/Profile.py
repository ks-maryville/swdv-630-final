from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column

from Final.User import User
from Final.db import *


class Profile(Base):
    __tablename__ = "profile"

    profile_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.user_id))
    # first_name: Mapped[Optional[str]]
    # middle_name: Mapped[Optional[str]]
    # last_name: Mapped[Optional[str]]
    profile_type: Mapped[str]

    __mapper_args__ = {
        "polymorphic_on": "profile_type",
        "polymorphic_identity": "profile"
    }



