#!/usr/bin/python3
"""base.py model contains the base class."""

import json


class Base(object):
    """Defines the Base class.

    Attributes:
        __nb_objects (int): Number of objects/instances.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the instance of base class.

        Args:
            id (int): id parameter
        """
        # Check if ID is not an int.
        if id is not None and not isinstance(id, int):
            raise TypeError("ID must be an integer.")

        # Check if id is None
        if id is None:
            self.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            # Check if ID is negative
            if id <= 0:
                raise ValueError("ID must be a non-zero  positive integer.")
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a dictionary into JSON string.

        Args:
            list_dictionaries (list/dict): list of dictionaries.
        """
        # check if list is None
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
