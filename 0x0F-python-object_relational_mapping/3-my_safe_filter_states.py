#!/usr/bin/python3
"""Select States filtered by user module SQL injection free"""
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
    query = "SELECT * FROM states \
        WHERE name COLLATE utf8mb4_bin LIKE %s \
        ORDER BY id"
    exe.execute(
        query,
        (search,)
    )
    link.commit()
    result = exe.fetchall()
    for res in result:
        print(res)
    exe.close()
    link.close()


if __name__ == "__main__":
    dbConnect()
