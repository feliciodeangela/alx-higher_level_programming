#!/usr/bin/python3
"""This module contains the definition of the Rectangle class."""


class Rectangle:
    """Rectangle class definition, responsible to design
    the blueprint of it's generation"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Rectangle class initialization.

        Args:
            width (int): Represents the Rectangle's width.
            height (int): Represents the Rectangle's height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances = self.number_of_instances + 1

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

    def area(self):
        """Rectangle's area calculator.

        Returns:
            The rectangle's area."""
        return (self.width * self.height)

    def perimeter(self):
        """Rectangle's perimeter calculator.

        Returns:
            The rectangle's perimeter."""
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * (self.width + self.height))

    def __str__(self):
        """Rectangle's str() method."""
        if self.width == 0 or self.height == 0:
            return ("")
        hsh = self.print_symbol * self.width
        #if isinstance(hsh, str):
        #    sp = "\n" + hsh
        #    return ("{}{}".format(hsh, sp * (self.height - 1)))
        #elif isinstance(hsh, list):
        #    sp = hsh.append(hsh * (self.height -1))
        #    return ([])
        return ([])

    def __repr__(self):
        """Rectangle's repr() method."""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """When a rectangle is destroied..."""
        print("Bye rectangle...")
        Rectangle.number_of_instances = self.number_of_instances - 1

    @classmethod
    def number_of_instances_updater(cls):
        """Number of instances updater."""
        return cls.number_of_instances

    @classmethod
    def print_symbol_updater(cls):
        """Print symbol updater."""
        return cls.print_symbol
