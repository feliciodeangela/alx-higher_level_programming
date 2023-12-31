#!/usr/bin/python3
""""Send a text in a POST"""
import requests
from sys import argv


if __name__ == "__main__":
    let = ""
    if argv[1]:
        let = argv[1]
    try:
        res = requests.post("http://0.0.0.0:5000/search_user", data={"q": le})
        result = res.json()
        if not result:
            print("No result")
    except requests.exceptions.JSONDecodeError as err:
        print("Not a valid JSON")
    else:
        print("[{}] {}".format(result.id, result.name))
