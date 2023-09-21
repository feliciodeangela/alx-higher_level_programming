#!/usr/bin/python3
"""This module contains the definition of the load_from_json_file function."""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): File/Directory containing the JSON.
    Returns:
        The object created from the JSON file."""
    with open(filename, "r+") as fl:
        return (json.load(fl))
