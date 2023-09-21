#!/usr/bin/python3
"""This module contains the definition of the class_to_json function"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj (obj): An instance of the class.
    Returns:
        Dictionary description of an object"""
    return (vars(obj))
