#!/usr/bin/python3
"""This module contains the definition of the Rectangle class."""


class Rectangle:
    """Rectangle class definition, responsible to design
    the blueprint of it's generation"""

    def __init__(self, width=0, height=0):
        """Rectangle class initialization.

        Args:
            width (int): Represents the Rectangle's width.
            height (int): Represents the Rectangle's height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Rectangle's width getter."""
        return (self.__width)

    @property
    def height(self):
        """Rectangle's height getter."""
        return (self.__height)

    @width.setter
    def width(self, value):
        """Rectangle's width setter.

        Args:
            value (int): The width's measure."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Rectangle's height setter.

        Args:
            value (int): The height's measure."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
