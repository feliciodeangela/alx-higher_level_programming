#!/usr/bin/python3
"""Select States filtered by user module"""
import MySQLdb
import sys


def dbConnect():
    """Database connection logic."""
    link = MySQLdb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            port=3306,
            host="localhost"
    )
    search = sys.argv[4]
    exe = link.cursor()
    exe.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id".
        format(search)
    )
    link.commit()
    result = exe.fetchall()
    for res in result:
        print(res)
    exe.close()
    link.close()


if __name__ == "__main__":
    dbConnect()
