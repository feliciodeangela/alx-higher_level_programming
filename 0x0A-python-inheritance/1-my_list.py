#!/usr/bin/python3
"""This module contains the MyList class definition."""


class MyList(list):
    """MyList definition."""

    def print_sorted(self):
        """Function to print a list in ascending order."""
        ll = self.copy()
        print(sorted(ll))
        return (sorted(ll))
