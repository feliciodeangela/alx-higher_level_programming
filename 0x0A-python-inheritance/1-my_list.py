#!/usr/bin/python3
"""This module contains the MyList class definition."""


class MyList(list):
    """MyList definition."""

    def print_sorted(self):
        """Function to print a list in ascending order."""
        print(sorted(self))

    def __str__(self):
        """str() method for MyList class."""
        return ("{}".format(self))
