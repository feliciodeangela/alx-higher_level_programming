#!/usr/bin/python3
"""This module contains the Base class definition."""


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
