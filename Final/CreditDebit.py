from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Final.Profile import Profile
from Final.db import *


class CreditDebit(Base):
    __tablename__ = "credit_debit"

    credit_debit_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    profile_id: Mapped[int] = mapped_column(ForeignKey(Profile.profile_id))
    card_number: Mapped[str]
    expiration: Mapped[str]
    cvv: Mapped[int]
    address_1: Mapped[str]
    address_2: Mapped[Optional[str]]
    city: Mapped[str]
    state: Mapped[str]
    zip: Mapped[str]
    date_created: Mapped[datetime]  # = mapped_column(default=datetime.now())
    date_updated: Mapped[Optional[datetime]]

    # relationships
    profile: Mapped["Profile"] = relationship(back_populates="payment_methods")

    def __init__(self, credit_debit_id, profile_id, card_number, expiration, cvv, address_1, address_2, city, state,
                 zip,
                 date_created, date_updated):
        self.credit_debit_id = credit_debit_id
        self.profile_id = profile_id
        self.card_number = card_number
        self.expiration = expiration
        self.cvv = cvv
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.zip = zip
        self.date_created = date_created
        self.date_updated = date_updated

    def __repr__(self):
        return f"(credit_debit_id: {self.credit_debit_id}, profile_id: {self.profile_id}, card_number: {self.card_number}, expiration: {self.expiration}, cvv: {self.cvv},address_1: {self.address_1},address_2: {self.address_2},city: {self.city},state: {self.state},zip: {self.zip}, date_created: {self.date_created},date_updated: {self.date_updated})"
