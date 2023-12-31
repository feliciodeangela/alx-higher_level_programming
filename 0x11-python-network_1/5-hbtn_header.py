#!/usr/bin/python3
"""Request and display value of a variable"""
from sys import argv
import requests


if __name__ == "__main__":
    resp = requests.get(argv[1])
    print(resp.headers['X-Request-Id'])
