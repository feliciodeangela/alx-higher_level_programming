#!/usr/bin/python3
"""POST a request and display part of the request's parameters in response"""
from sys import argv
import requests


if __name__ == "__main__":
    resp = requests.post(argv[1], data={'email': argv[2]})
    print(resp.content.decode("utf8"))
