#!/usr/bin/python3
"""Script that lists all State objects that contain the letter a from
 the database"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def dbConnect():
    """Connection and filtered selection query logic"""
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
    link = Session()
    search = 'a'
    result = link.query(State).filter(State.name.like("%{}%".format(search)))\
        .order_by(State.id)
    for res in result:
        print("{}: {}".format(res.id, res.name))


if __name__ == "__main__":
    dbConnect()
