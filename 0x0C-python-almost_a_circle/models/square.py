#!/usr/bin/python3
"""
square.py

A module that contains a subclass that inherites form a Rectangle class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A subclass that inherites from the Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates an object of a Square subclass.

        Args:
            size (int): size of sides of a Square.
            x (int): horizontal coordinate of a Square.
            y (int): Vertical coordinate of a square.
            id (int): ID of the object.
        """
        super().__init__(size, size, x, y, id)

        @property
        def size(self):
            """Gets the size of the Square.

            Returns:
                int: size of the Square.
            """
            return self.width

        @size.setter
        def size(self, size):
            """Sets the size of the Square.

            Args:
                size (int): size of the Square.
            """
            self.height = size
            self.width = size

        def __str__(self):
            """String Representantion of a Square.

            Returns:
                str: string representantion of a Square.
            """
            return "[Square] ({}) {}/{} - {}".format(
                    self.id, self.x, self.y, self.height)
