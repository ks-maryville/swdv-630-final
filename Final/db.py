from sqlalchemy import create_engine, text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///sqlite.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class DB:
    @classmethod
    def save(cls, instance):
        try:
            session.add(instance)
            session.commit()
        except IntegrityError:
            print("error")
            session.rollback()

    @classmethod
    def get_all(cls):
        print("printing ALL")
        objects = []
        result = session.query(cls).all()
        for row in result:
            objects.append(row)

        return objects

    @classmethod
    def get_by_pk(cls, pk):
        result = session.query(cls).get(pk)
        print(result)
        return result
