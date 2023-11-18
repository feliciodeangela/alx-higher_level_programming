#!/usr/bin/python3
"""Filtered states selection module"""
import sys
import MySQLdb


def dbConnect():
    """Filtered states selection function"""
    link = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        host="localhost",
        port=3306
    )
    exe = link.cursor()
    exe.execute(
            "SELECT * FROM states \
            WHERE name COLLATE utf8mb4_bin LIKE'N%' \
            ORDER BY id",
    )
    result = exe.fetchall()
    for res in result:
        print(res)
    exe.close()
    link.close()


if __name__ == "__main__":
    dbConnect()
