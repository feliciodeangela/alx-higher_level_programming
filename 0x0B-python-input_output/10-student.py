#!/usr/bin/python3
"""This module contains the definition of the Student class"""


class Student:
    """Student clas definition"""

    def __init__(self, first_name, last_name, age):
        """Student class contructor

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves the dict() representation of Student

        Args:
            attrs (list): List of (str) attributes.
        Returns:
            The Student's dict()"""
        sattrs = ["first_name", "last_name", "age"]
        sdict = {}
        i = 0
        if isinstance(attrs, list):
            for c in attrs:
                if isinstance(attrs[i], str) and attrs[i] in sattrs:
                    if attrs[i] == "first_name":
                        sdict[attrs[i]] = self.first_name
                    if attrs[i] == "last_name":
                        sdict[attrs[i]] = self.last_name
                    if attrs[i] == "age":
                        sdict[attrs[i]] = self.age
                i = i + 1
            return (sdict)
        return ({'first_name': self.first_name,
                 'last_name': self.last_name, 'age': self.age})
