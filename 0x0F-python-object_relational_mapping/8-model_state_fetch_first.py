#!/usr/bin/python3
"""Script to print the first State object from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def dbConnect():
    """Connection and query for selection logic"""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1],
            argv[2],
            argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id).first()
    if result:
        print("{}: {}".format(result.id, result.name))
    else:
        print('Nothing')


if __name__ == "__main__":
    dbConnect()
