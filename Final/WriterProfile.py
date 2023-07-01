from typing import List, Optional

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Final.Profile import Profile
from Final.db import *


class WriterProfile(Profile):
    is_writer: Mapped[bool] = mapped_column(nullable=True)
    articles: Mapped[Optional[List["Article"]]] = relationship(backref="Profile")
    __mapper_args__ = {
        "polymorphic_identity": "writer"
    }

    def __init__(self, profile_id, user_id, profile_type, is_writer):
        self.profile_id = profile_id
        self.user_id = user_id
        # self.first_name = first_name
        # self.middle_name = middle_name
        # self.last_name = last_name
        self.profile_type = profile_type
        self.is_writer = is_writer

    def __repr__(self):
        return f"(profile_id: {self.profile_id},user_id: {self.user_id},profile_type: {self.profile_type},is_writer: {self.is_writer})"

    def create_article(self):
        pass

    def submit_article(self):
        pass
