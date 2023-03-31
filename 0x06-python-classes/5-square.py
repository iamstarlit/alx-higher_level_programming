#!/usr/bin/python3

# 0-square.py by Paul John
"""A module that defines a square"""


class Square(object):
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializes this Square Class
        Args:
            size - size of the square defined
        """

        self.size = size

    @property
    def size(self):
        """Retrives size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the value of size of the square safely"""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """
        Calculates the area of the square
        Returns: The square of size
        """

        return (self.__size ** 2)

    def my_print(self):
        """print the square in # """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
