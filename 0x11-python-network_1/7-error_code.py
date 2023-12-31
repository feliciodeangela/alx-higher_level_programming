#!/usr/bin/python3
"""Send request and show error if it hapens"""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        resp = requests.get(argv[1])
        print(resp.content.decode("utf8"))
    except requests.exceptions.HTTPError as err:
        print("Error code: {}".format(err))
