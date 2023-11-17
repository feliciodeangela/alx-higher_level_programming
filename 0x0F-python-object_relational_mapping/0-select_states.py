#!/usr/bin/python3
"""Select States module"""
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
    exe = link.cursor()
    exe.execute("SELECT * FROM states ORDER BY id")
    link.commit()
    result = exe.fetchall()
    for res in result:
        print(res)
    exe.close()
    link.close()


if __name__ == "__main__":
    dbConnect()
