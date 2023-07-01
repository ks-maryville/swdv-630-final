from datetime import datetime
from typing import Optional, List

from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Final.User import User
from Final.Comment import Comment
from Final.Profile import Profile
from Final.EditorProfile import EditorProfile
from Final.db import *


class Article(Base):
    __tablename__ = "article"

    article_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    body: Mapped[str]
    edited: Mapped[Optional[bool]]
    approved: Mapped[Optional[bool]]
    likes: Mapped[Optional[int]] = mapped_column(default=0)
    dislikes: Mapped[Optional[int]] = mapped_column(default=0)
    date_created: Mapped[datetime]
    date_updated: Mapped[Optional[datetime]]

    # Relationships
    profile_id: Mapped[int] = mapped_column(ForeignKey(Profile.profile_id))
    editor_id: Mapped[Optional[int]] = mapped_column(ForeignKey(User.user_id))
    comments: Mapped[Optional[List[Comment]]] = relationship(back_populates="article")

    def __init__(self, article_id, profile_id, editor_id, title, body, edited, approved, likes, dislikes, comments,
                 date_created, date_updated):
        self.article_id = article_id
        self.profile_id = profile_id
        self.editor_id = editor_id
        self.title = title
        self.body = body
        self.edited = edited
        self.approved = approved
        self.likes = likes
        self.dislikes = dislikes
        self.comments = comments
        self.date_created = date_created
        self.date_updated = date_updated

    def __repr__(self):
        return f"(article_id: {self.article_id}\nprofile_id: {self.profile_id}\neditor_id: {self.editor_id}\ntitle: {self.title}\nbody: {self.body}\nedited: {self.edited}\napproved: {self.approved}\nlikes: {self.likes}\ndislikes: {self.dislikes}\ncomments: {self.comments}\ndate_created: {self.date_created}\ndate_updated: {self.date_updated})"

    def get_likes(self):
        pass

    def get_dislikes(self):
        pass
