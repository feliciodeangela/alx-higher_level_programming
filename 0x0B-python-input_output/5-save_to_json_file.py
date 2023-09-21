#!/usr/bin/python3
"""This module contains the definition of the save_to_json_file."""
import json


def save_to_json_file(my_obj, filename=""):
    """Writes an object to a text file using a JSON representation."""
    with open(filename, "w") as fl:
        json.dump(my_obj,fl)
