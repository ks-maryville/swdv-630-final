from datetime import datetime
from typing import Optional, List

from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

# from Final.Article import Article
from Final.Profile import Profile
from Final.User import User
from Final.db import *


class Comment(Base):
    __tablename__ = "comment"

    comment_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    body: Mapped[str]
    likes: Mapped[Optional[int]] = mapped_column(default=0)
    dislikes: Mapped[Optional[int]] = mapped_column(default=0)
    date_created: Mapped[datetime]
    date_updated: Mapped[Optional[datetime]]

    # Relationships
    article_id: Mapped[int] = mapped_column(ForeignKey("article.article_id"))
    profile_id: Mapped[int] = mapped_column(ForeignKey("profile.profile_id"))
    article: Mapped["Article"] = relationship(back_populates="comments")

    def __init__(self, comment_id, article_id, profile_id, body, likes, dislikes,
                 date_created, date_updated):
        self.comment_id = comment_id
        self.article_id = article_id
        self.profile_id = profile_id
        self.body = body
        self.likes = likes
        self.dislikes = dislikes
        self.date_created = date_created
        self.date_updated = date_updated

    def __repr__(self):
        return f"(comment_id: {self.comment_id}\narticle_id : {self.article_id}\nprofile_id : {self.profile_id}\nbody: {self.body}\nlikes: {self.likes}\ndislikes: {self.dislikes}\ndate_created: {self.date_created}\ndate_updated: {self.date_updated})"
