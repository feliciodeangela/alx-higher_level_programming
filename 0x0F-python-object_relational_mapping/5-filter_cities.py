#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and lists \
all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv


def dbConnect():
    """Selection query with user input as search parameter"""
    link = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3],
        host="localhost",
        port=3306
    )
    search = argv[4]
    exe = link.cursor()
    exe.execute(
        "SELECT cities.name FROM cities\
         JOIN states ON cities.state_id = states.id\
         WHERE states.name COLLATE utf8mb4_bin LIKE %s\
         ORDER BY cities.id",
        (search,)
    )
    link.commit()
    result = exe.fetchall()
    if len(result) == 0:
        print()
    for i in range(0, len(result)):
        if i < (len(result) - 1):
            print(result[i][0], end=', ')
        else:
            print(result[i][0])
    exe.close()
    link.close()


if __name__ == "__main__":
    dbConnect()
