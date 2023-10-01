#!/usr/bin/python3
"""This module contains the Base class definition."""
from json import dumps, loads


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Transform string to json obj
        Args:
            list_dictionaries (list): List of dictionaries"""
        if list_dictionaries is None:
            return ('[]')
        else:
            return (dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Save objects to file"""
        with open(cls.__name__ + '.json', 'w') as fl:
            if list_objs is None:
                fl.write('[]')
            else:
                fl.write(cls.to_json_string([lob.to_dictionary()
                                             for lob in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None:
            return ([])
        return (loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with set attributes"""
        if cls.__name__ == "Square":
            dummy = cls(2)
        else:
            dummy = cls(2, 3)
        dummy.update(**dictionary)
        return(dummy)
