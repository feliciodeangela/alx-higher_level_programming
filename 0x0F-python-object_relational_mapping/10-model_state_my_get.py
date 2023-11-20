#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument from
 the database"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def dbConnect():
    """Connection and select query logic based on user input"""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1],
            argv[2],
            argv[3]
        ),
        pool_pre_ping=True
    )
    search = argv[4]
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    link = Session()
    result = link.query(State).filter(State.name.like("{}".format(search)))
    if result:
        for res in result:
            print("{}".format(res.id))
    else:
        print('Not found')


if __name__ == "__main__":
    dbConnect()
