#!/usr/bin/python3
"""This module contains the definition of the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class definition"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class contructor
        Args:
            size (int):
            x (int):
            y (int):
            id (int):"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Returns the string representation of the Square"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """Square's attributes updater"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for keys, val in kwargs.items():
                setattr(self, keys, val)

    def to_dictionary(self):
        """Return the dict() representation of the Square"""
        dct = {}
        for attr in ['id', 'size', 'x', 'y']:
            dct[attr] = getattr(self, attr)
        return dct

    @property
    def size(self):
        """Sqaure's size getter"""
        return (self.width)

    @size.setter
    def size(self, size):
        """Square's size setter
        Args:
            size (int):"""
        self.width = size
        self.height = size
