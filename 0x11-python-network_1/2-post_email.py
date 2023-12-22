#!/usr/bin/python3
"""Send a POST request"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    email = argv[2]
    data = parse.urlencode({"email": email})
    data = data.encode("utf8")
    req = request.Request(argv[1], data)
    with request.urlopen(req) as resp:
        print("Your email is: {}".format(resp.read().decode("utf8")))
