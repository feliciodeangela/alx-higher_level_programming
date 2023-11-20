#!/usr/bin/python3
"""Script that deletes all State objects with a name containing the letter a
from the database"""
from sys import argv
from sqlalchemy import delete, create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def dbConnect():
    """Function containing deletion query logic"""
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
    chars = 'a'
    # link.query(State).filter(State.name.like("%{}%".format(chars)))
    link.execute(delete(State).where(State.name.like("%{}%".format(chars))))
    link.commit()


if __name__ == "__main__":
    dbConnect()
