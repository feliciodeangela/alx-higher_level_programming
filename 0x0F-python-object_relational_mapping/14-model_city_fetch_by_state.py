#!/usr/bin/python3
"""Module containing function to print Cities"""
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sys import argv


def dbConnect():
    """Function to print all City objects from the database"""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1],
            argv[2],
            argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    link = Session()
    result = link.query(City, State)\
        .filter(City.state_id == State.id)\
        .order_by(City.id)
    for res1, res2 in result:
        print("{}: ({}) {}".format(res2.name, res1.id, res1.name))


if __name__ == "__main__":
    dbConnect()
