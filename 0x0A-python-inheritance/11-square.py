#!/usr/bin/python3
"""This module contains the definition of the Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class definition.

    Args:
        Rectangle: (parent)Rectangle class."""

    def __init__(self, size):
        """Square class contructor."""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Square's are calculator.

        Returns:
            Square's area."""
        return (self.__size * self.__size)

    def __str__(self):
        """str() function for Square class."""
        return ("[{0}] {1}/{1}".format(type(self).__name__, self.__size))
