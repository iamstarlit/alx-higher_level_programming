#!/usr/bin/python3
"""
A module that contains Square Sub Class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Sub Class of Rectangle, Square."""

    def __init__(self, size):
        """Initializes an instance of Square Sub Class.

        Args:
           Size: size of square
        
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Computes area of a Square."""

        return super().area()
