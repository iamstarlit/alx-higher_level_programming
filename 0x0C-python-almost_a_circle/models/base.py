#!/usr/bin/python3
"""base.py model contains the base class."""


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
        # Check if id is None
        if id:
            self.id = id
        else:
            # Increment no of objects.
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
