from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column

from Final.Profile import Profile
from Final.db import *


class AdministratorProfile(Profile):
    is_administrator: Mapped[bool] = mapped_column(nullable=True)
    __mapper_args__ = {
        "polymorphic_identity": "admin"
    }

    def __init__(self, profile_id, user_id, first_name, middle_name, last_name, profile_type, is_administrator):
        super().__init__(profile_id, user_id, first_name, middle_name, last_name, profile_type)
        self.is_administrator = is_administrator

    def __repr__(self):
        # return f"(profile_id: {self.profile_id},user_id: {self.user_id},profile_type: {self.profile_type},is_administrator: {self.is_administrator})"
        return str(self.__dict__)
