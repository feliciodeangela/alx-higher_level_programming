#!/usr/bin/python3
"""Authenticate and display my github id"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/users/{}".format(argv[1])
    hdr = {"Authorization": "token {}".format(argv[2])}
    resp = requests.get(url, headers=hdr)
    print(resp.json())
