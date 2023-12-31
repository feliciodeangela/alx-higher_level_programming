#!/usr/bin/python3
""""Send a text in a POST"""
import requests
from sys import argv


if __name__ == "__main__":
    le = ""
    if len(argv) > 1:
        le = argv[1]
    try:
        res = requests.post("http://0.0.0.0:5000/search_user", data={"q": le})
        result = res.json()
        if not result:
            print("No result")
        else:
            print("[{}] {}".format(result.get('id'), result.get('name')))
    except requests.JSONDecodeError as err:
        print("Not a valid JSON")
