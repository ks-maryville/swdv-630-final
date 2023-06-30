# from typing import Optional
#
# from sqlalchemy import Column, Integer, ForeignKey, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from Final.SubscriberProfile import SubscriberProfile


# from Final.User import User
# from Final.db import DB, engine


# class Base(DeclarativeBase):
#     pass


class ProfileFactory:
    __abstract__ = True

    @staticmethod
    def create_profile(role, *args):
        if role == 'Subscriber':
            return SubscriberProfile(*args)
        elif role == "Writer":
            pass
            # return WriterProfile()
        elif role == "Editor":
            pass
            # return EditorProfile()
        elif role == "Admin":
            pass
            # return AdminProfile()

# Base.metadata.drop_all(bind=engine)

# Base.metadata.create_all(bind=engine)
