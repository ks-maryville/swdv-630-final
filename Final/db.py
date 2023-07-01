from sqlalchemy import create_engine, text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

engine = create_engine("sqlite:///sqlite.db", echo=True, echo_pool='debug')
Session = sessionmaker(bind=engine)
session = Session()
# print("session", session.dirty)
