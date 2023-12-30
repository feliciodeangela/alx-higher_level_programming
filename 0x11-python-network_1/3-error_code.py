#!/usr/bin/python3
"""Show body of response and take care of error codes"""
from urllib import error, request
from sys import argv


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as resp:
            print("{}".format(resp.read().decode("utf8")))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
