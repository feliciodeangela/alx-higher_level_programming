#!/usr/bin/python3
"""Script that adds the State object 'Louisiana' to the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


def dbConnect():
    """Logic to add an object to the table"""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1],
            argv[2],
            argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    stateName = "Louisiana"
    Session = sessionmaker(bind=engine)
    link = Session()
    newState = State(name=stateName)
    link.add(newState)
    link.commit()
    result = link.query(State).filter(State.name.like(stateName)).first()
    print(result.id)


if __name__ == "__main__":
    dbConnect()
