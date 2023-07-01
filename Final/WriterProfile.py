from datetime import datetime
from typing import List, Optional

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Final.Article import Article
from Final.Profile import Profile
from Final.db import *


class WriterProfile(Profile):
    is_writer: Mapped[bool] = mapped_column(nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "writer"
    }

    # Relationships

    def __init__(self, profile_id, user_id, first_name, middle_name, last_name, profile_type, is_writer, articles):
        super().__init__(profile_id, user_id, first_name, middle_name, last_name, profile_type)
        self.is_writer = is_writer
        self.articles = articles

    def __repr__(self):
        return f"(profile_id: {self.profile_id},user_id: {self.user_id},first_name: {self.first_name},middle_name: {self.middle_name},last_name: {self.last_name},profile_type: {self.profile_type},is_writer: {self.is_writer}, articles: {self.articles})"

    def create_article(self, title, body):
        return Article(None, self.profile_id, None, title, body, False, False, False, 0, 0, [], datetime.now())

    def submit_article(self, article):
        article.submitted = True
        article.date_updated = datetime.now()