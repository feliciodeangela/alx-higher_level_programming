#!/usr/bin/python3
"""Send request and show error if it hapens"""
import requests
from sys import argv


if __name__ == "__main__":
    resp = requests.get(argv[1])
    if resp.status_code >= 400:
        print(resp.status_code)
    else:
        print(resp.content.decode("utf8"))
