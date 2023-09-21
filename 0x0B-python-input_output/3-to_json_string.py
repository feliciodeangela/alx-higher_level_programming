#!/usr/bin/python3
"""This module contains the definition of the to_json_string."""
import json


def to_json_string(my_obj):
    """Function that returns the JSON representation of a string object.

    Args:
        my_obj (str): String object to transform into json.
    Returns:
        The json representation of the string object."""
    return (json.dumps(my_obj))
