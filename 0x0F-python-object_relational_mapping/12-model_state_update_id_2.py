#!/usr/bin/python3
"""Script that changes the name of a State object from the database"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def dbConnect():
    """Connection and update query logic"""
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
    stateID = 2
    newState = "New Mexico"
    toUpdate = link.query(State).filter(State.id == stateID).update(
        {State.name: newState},
        synchronize_session=False
    )


if __name__ == "__main__":
    dbConnect()
