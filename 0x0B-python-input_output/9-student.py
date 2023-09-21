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

    def to_json(self):
        """Retrieves the dict() representation of Student

        Returns:
            The Student's dict()"""
        return ({'first_name': self.first_name, \
                'last_name': self.last_name, 'age': self.age})
