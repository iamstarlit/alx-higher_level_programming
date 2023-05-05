#!/usr/bin/python3
"""
square.py

This module contains the Square class, which inherits from the Rectangle class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, which is a special kind of rectangle where
    the width and height are equal.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square object.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): The ID of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the square with the given arguments.

        Args:
            *args: The arguments to update the square with.
            **kwargs: The keyword arguments to update the square with.
        """
        if args:
            list_atr = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, list_atr[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if 'size' in kwargs:
            self.width = kwargs['size']
            self.height = kwargs['size']

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square.

        Returns:
            dict: A dictionary representation of the square.
        """
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
