#!/usr/bin/python3

"""my module solve area and circumference of circle"""
import math


class MagicClass(object):
    """Magic calculation class"""

    def __init__(self, radius=0):
        """Initilizes the the radius"""

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """calculates area of the circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """calculates circumference of the circle"""
        return (2 * math.pi * self.__radius)
