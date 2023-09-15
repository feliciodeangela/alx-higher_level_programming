#!/usr/bin/python3
    """This module contains the definition of the Rectangle class."""


class Rectangle:
    """Rectangle class definition."""

    def __init__(self, width=0, height=0):
        """Rectangle class initialization.

        Args:
            width (int): Represents the Rectangle's width.
            height (int): Represents the Rectangle's heigth."""
        if not isinstance(width, int):
            raise TypeError("width must be a number")
        if not isinstance(heigth, int):
            raise TypeError("height must be a number")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
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
        self.__width = value

    @height.setter
    def height(self, value):
        """Rectangle's height setter.

        Args:
            value (int): The height's measure."""
        self.__height = value
