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
