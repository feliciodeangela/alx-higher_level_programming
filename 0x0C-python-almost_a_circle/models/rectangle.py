#!/usr/bin/python3
"""This module contains the Rectangle's class definition"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class definition"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle's class constructor
        Args:
            width (int): Rectangle's width.
            height (int): Rectangle's height.
            x (int):
            y (int):"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """Rectangle's area calculator"""
        return (self.width * self.height)

    def display(self):
        """Prints a representation of the instance"""
        cc = " " * self.x
        ccc = "" * self.y
        [print('') for y in range(self.y)]
        c = cc + "#" * self.width
        sp = "\n" + c
        print("{}{}".format(c, sp * (self.height - 1)))

    def __str__(self):
        """Returns the string representation of the Rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Rectangle's data updater."""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for keys, val in kwargs.items():
                setattr(self, keys, val)

    @property
    def width(self):
        """Rectangle's width getter"""
        return (self.__width)

    @property
    def height(self):
        """Rectangle's height getter"""
        return (self.__height)

    @property
    def x(self):
        """Rectangle's x getter"""
        return (self.__x)

    @property
    def y(self):
        """Rectangle's y getter"""
        return (self.__y)

    @width.setter
    def width(self, width):
        """Rectangle's width setter
        Args:
            width (int):"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Rectangle's height setter
        Args:
            height (int):"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """Rectangle's x setter
        Args:
            x (int):"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """Rectangle's y setter
        Args:
            y (int)"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
