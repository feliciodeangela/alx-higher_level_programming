#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv


def dbConnect():
    """Selection query logic"""
    link = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3],
        host="localhost",
        port=3306
    )
    exe = link.cursor()
    exe.execute(
        "SELECT cities.id, cities.name, states.name FROM cities\
         JOIN states ON cities.state_id = states.id\
         ORDER BY cities.id"
    )
    result = exe.fetchall()
    link.commit()
    for res in result:
        print(res)
    exe.close()
    link.close()


if __name__ == "__main__":
    dbConnect()
