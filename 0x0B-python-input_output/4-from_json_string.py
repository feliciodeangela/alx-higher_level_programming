#!/usr/bin/python3
"""This module contains the definition of the from_json_string."""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
        my_str (str): JSON string.
    Returns:
        A python object."""
    return (json.loads(my_str))
