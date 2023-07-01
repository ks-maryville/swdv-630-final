from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Final.Profile import Profile
from Final.db import *


class Subscription(Base):
    __tablename__ = "subscription"

    subscription_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    profile_id: Mapped[int] = mapped_column(ForeignKey(Profile.profile_id))
    price: Mapped[float]
    date_created: Mapped[datetime]  # = mapped_column(default=datetime.now())
    date_updated: Mapped[Optional[datetime]]

    # relationships
    profile: Mapped["Profile"] = relationship(back_populates="subscription")

    def __init__(self, subscription_id, profile_id, price,
                 date_created, date_updated):
        self.subscription_id = subscription_id
        self.profile_id = profile_id
        self.price = price
        self.date_created = date_created
        self.date_updated = date_updated

    def __repr__(self):
        return f"(subscription_id: {self.subscription_id}, profile_id: {self.profile_id}, price: {self.price}, date_created: {self.date_created},date_updated: {self.date_updated})"
