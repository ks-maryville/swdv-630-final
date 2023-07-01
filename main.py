import datetime
import uuid

from colorama import Fore, Back
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
        print("============ creating users =============")
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
                    print(f"(============ creating {user.role} profile =============)")
                    profile = AdministratorProfile(1, user.user_id, "first_name", "middle_name", "last_name", user.role,
                                                   True)
                    session.add(profile)
                    session.commit()
                elif user.role == 'subscriber':
                    print(f"(============ creating {user.role} profile =============)")
                    profile = SubscriberProfile(2, user.user_id, "first_name", "middle_name", "last_name", user.role,
                                                True)
                    session.add(profile)
                    session.commit()
                elif user.role == 'writer':
                    print(f"(============ creating {user.role} profile =============)")
                    profile = WriterProfile(3, user.user_id, "first_name", "middle_name", "last_name", user.role, True,
                                            [])
                    session.add(profile)
                    session.commit()
                elif user.role == 'editor':
                    print(f"(============ creating {user.role} profile =============)")
                    profile = EditorProfile(4, user.user_id, "first_name", "middle_name", "last_name", user.role, True)
                    session.add(profile)
                    session.commit()

        # writer creates article and saves it to the database
        test_writer = session.query(WriterProfile).get(3)
        test_new_article = test_writer.create_article("newArticle", "articleBody")
        session.add(test_new_article)
        session.commit()
        # writer submits the article for editing (setting the article to "submitted" then updating the row)
        article_to_submit = session.query(Article).get(1)
        test_writer.submit_article(article_to_submit)
        session.commit()
        print(Fore.GREEN)
        print(session.query(WriterProfile).get(3))
        # editor edits and submits the article
        test_editor = session.query(EditorProfile).get(4)
        get_article = session.query(Article).get(1)
        print(get_article)
        test_editor.edit_article(get_article, "Edits have been made")
        session.commit()
        test_editor.submit_article(get_article)
        session.commit()
        print(Fore.BLUE)
        print(get_article)
        # administrator approves the article for posting
        test_admin = session.query(AdministratorProfile).get(1)
        article_to_approve = session.query(Article).get(1)
        print(article_to_approve)
        test_admin.approve_article(article_to_approve)
        session.commit()
        print(Fore.MAGENTA)
        print(article_to_approve)
        # subscriber adds comment to the article
        test_subscriber = session.query(SubscriberProfile).get(2)
        article_for_comment = session.query(Article).get(1)
        print(article_for_comment)
        test_comment = test_subscriber.add_comment(article_for_comment.article_id, "This is a great article!")
        session.add(test_comment)
        session.commit()
        print(Fore.CYAN)
        print(article_for_comment)
    except IntegrityError:
        error = SQLAlchemyError()
        print("error")
        session.rollback()


if __name__ == "__main__":
    main()
