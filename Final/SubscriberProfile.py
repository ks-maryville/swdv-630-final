from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column

from Final.Comment import Comment
from Final.CreditDebit import CreditDebit
from Final.Profile import Profile
from Final.Subscription import Subscription
from Final.db import *


class SubscriberProfile(Profile):
    has_subscription: Mapped[bool] = mapped_column(nullable=True)
    __mapper_args__ = {
        "polymorphic_identity": "subscriber"
    }

    # relationships
    def __init__(self, profile_id, user_id, first_name, middle_name, last_name, profile_type,
                 has_subscription,
                 subscription):
        super().__init__(profile_id, user_id, first_name, middle_name, last_name, profile_type)

        self.has_subscription = has_subscription
        self.subscription = subscription

    def __repr__(self):
        return f"(profile_id: {self.profile_id},user_id: {self.user_id},profile_type: {self.profile_type},has_subscription: {self.has_subscription}), payment_methods: {self.payment_methods}, subscription: {self.subscription}"

    def add_comment(self, article_id, body):
        return Comment(None, article_id, self.profile_id, body, likes=0, dislikes=0, date_created=datetime.now(),
                       date_updated=None)

    def add_subscription(self):
        return Subscription(None, self.profile_id, 10.99, datetime.now(), None)

    # future implementation
    def add_payment_method(self, card_number, expiration, cvv, address_1, address_2, city, state, zip):
        return CreditDebit(None, self.profile_id, card_number, expiration, cvv, address_1, address_2,
                           city, state, zip, datetime.now(), None)
