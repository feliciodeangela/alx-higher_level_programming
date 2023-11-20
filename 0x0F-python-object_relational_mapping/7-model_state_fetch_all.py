#!/usr/bin/python3
"""Get all states via SQLAlchemy"""
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session, sessionmaker


def dbConnect():
    """Function containing query and connection logic."""
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
    result = session.query(State).all()
    for res in result:
        print("{}: {}".format(res.id, res.name))


if __name__ == "__main__":
    dbConnect()
