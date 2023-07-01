from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column

from Final.Profile import Profile
from Final.db import *


class EditorProfile(Profile):
    is_editor: Mapped[bool] = mapped_column(nullable=True)
    __mapper_args__ = {
        "polymorphic_identity": "editor"
    }

    def __init__(self, profile_id, user_id, first_name, middle_name, last_name, profile_type, is_editor):
        super().__init__(profile_id, user_id, first_name, middle_name, last_name, profile_type)
        self.is_editor = is_editor

    def __repr__(self):
        return f"(profile_id: {self.profile_id},user_id: {self.user_id},profile_type: {self.profile_type},is_editor: {self.is_editor})"

    def edit_article(self, article, new_body_text):
        article.body = new_body_text
        article.date_updated = datetime.now()

    def submit_article(self, article):
        article.edited = True
