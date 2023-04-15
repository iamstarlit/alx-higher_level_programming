#!/usr/bin/python3
"""
10-student.py

A module that defines a Student class.
"""


class Student(object):
    """A class that represents a Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student object.

        Args:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrive dictionary representantion of Student class.

        Args:
            attrs (list: 'str'): attribute names
        Returns:
            dict: if attr is a list, return names, otherwise
            return whole dictionary.
        """
        if (type(attrs) == list and all(type(item) == str for item in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}

        return self.__dict__
