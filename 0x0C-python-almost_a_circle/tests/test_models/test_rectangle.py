#!/usr/bin/python3
"""
test_reactangle.py

Performs unit tests for the Reactangle Class.
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class."""

    def test_rectangle_init(self):
        """Tests `width` attribute from the Base class."""
        r1 = Rectangle(10, 5, 1, 2, 25)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 25)

    def test_id(self):
        """Test `id` attribute from the base class."""
        r2 = Rectangle(10, 20)

        self.assertEqual(r2.id, 1)
