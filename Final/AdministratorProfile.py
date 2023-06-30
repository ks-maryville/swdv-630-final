from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column

from Final.Profile import Profile
from Final.db import *


class AdministratorProfile(Profile):
    is_administrator: Mapped[bool] = mapped_column(nullable=True)
    __mapper_args__ = {
        "polymorphic_identity": "admin"
    }

    def __init__(self, profile_id, user_id, profile_type, is_administrator):
        self.profile_id = profile_id
        self.user_id = user_id
        # self.first_name = first_name
        # self.middle_name = middle_name
        # self.last_name = last_name
        self.profile_type = profile_type
        self.is_administrator = is_administrator

    def __repr__(self):
        return f"(profile_id: {self.profile_id},user_id: {self.user_id},profile_type: {self.profile_type},is_administrator: {self.is_administrator})"
