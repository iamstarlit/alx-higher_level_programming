#!/usr/bin/python3
"""
9-student.py

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

    def to_json(self):
        """Retrive dictionary representantion of Student class."""
        return self.__dict__
