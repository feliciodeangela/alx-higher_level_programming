#!/usr/bin/python3
"""This module contains the Base class definition."""
from json import dumps


class Base:
    """Base class definition"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor

        Args:
            id (int): Object instance id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Transform string to json obj
        Args:
            list_dictionaries (list): List of dictionaries"""
        if list_dictionaries is None:
            return ("[]")
        else:
            return (dumps(list_dictionaries))
