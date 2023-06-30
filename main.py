from colorama import Fore
from sqlalchemy.exc import SQLAlchemyError

from Final.AdministratorProfile import AdministratorProfile
from Final.EditorProfile import EditorProfile
from Final.SubscriberProfile import SubscriberProfile
from Final.User import *
from Final.WriterProfile import WriterProfile
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

                    profile = AdministratorProfile(None, user.user_id, user.role, True)
                    session.add(profile)
                    session.commit()
                elif user.role == 'subscriber':
                    print(Fore.YELLOW + f"(============ creating {user.role} profile =============)")
                    profile = SubscriberProfile(None, user.user_id, user.role, True)
                    session.add(profile)
                    session.commit()
                elif user.role == 'writer':
                    print(Fore.YELLOW + f"(============ creating {user.role} profile =============)")
                    profile = WriterProfile(None, user.user_id, user.role, True)
                    session.add(profile)
                    session.commit()
                elif user.role == 'editor':
                    print(Fore.YELLOW + f"(============ creating {user.role} profile =============)")
                    profile = EditorProfile(None, user.user_id, user.role, True)
                    session.add(profile)
                    session.commit()

        query = session.query(User).all()
        print(Fore.MAGENTA + "This query is NULL: ", query is None)
        print(Fore.MAGENTA + query.__str__())

        print("=========================================")

    except IntegrityError:
        error = SQLAlchemyError()
        print("error")
        session.rollback()


if __name__ == "__main__":
    main()
