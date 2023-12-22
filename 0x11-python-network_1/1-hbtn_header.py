#!/usr/bin/python3
"""Get value of a specific variable"""
from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as resp:
        print(resp.info()["X-Request-Id"])
