import datetime
import uuid

from colorama import Fore
from sqlalchemy.exc import SQLAlchemyError

from Final.User import *
from Final.AdministratorProfile import AdministratorProfile
from Final.SubscriberProfile import SubscriberProfile
from Final.EditorProfile import EditorProfile
from Final.WriterProfile import WriterProfile
from Final.Article import Article
from Final.db import *


def main():
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    try:
        print(Fore.BLUE + "============ creating users =============")
        # instantiate new users
        admin = User(1, "admin@email.com", "password", "admin")
        subscriber = User(2, "newGuy@email.com", "password", "subscriber")
        writer = User(3, "thisguy@email.com", "password", "writer")
        editor = User(4, "thatguy@email.com", "password", "editor")

        users = [admin, subscriber, writer, editor]
        for user in users:
            query = session.query(User).filter_by(email=user.email).first()
            if query is None:
                session.add(user)
                if user.role == 'admin':
                    print(Fore.YELLOW + f"(============ creating {user.role} profile =============)")
                    profile = AdministratorProfile(1, user.user_id, user.role, True)
                    session.add(profile)
                    session.commit()
                elif user.role == 'subscriber':
                    print(Fore.YELLOW + f"(============ creating {user.role} profile =============)")
                    profile = SubscriberProfile(2, user.user_id, user.role, True)
                    session.add(profile)
                    session.commit()
                elif user.role == 'writer':
                    print(Fore.YELLOW + f"(============ creating {user.role} profile =============)")
                    profile = WriterProfile(3, user.user_id, user.role, True)
                    session.add(profile)
                    session.commit()
                elif user.role == 'editor':
                    print(Fore.YELLOW + f"(============ creating {user.role} profile =============)")
                    profile = EditorProfile(4, user.user_id, user.role, True)
                    session.add(profile)
                    session.commit()

        query = session.query(User).all()
        print(Fore.MAGENTA + "This query is NULL: ", query is None)
        print(Fore.MAGENTA + query.__str__())

        print("=========================================")
        article = Article(None, 3, None, "title", "body", None, None, None, None,[], datetime.datetime.now(), None)
        session.add(article)
        session.commit()
        print(session.query(Article).all())
    except IntegrityError:
        error = SQLAlchemyError()
        print("error")
        session.rollback()


if __name__ == "__main__":
    main()
