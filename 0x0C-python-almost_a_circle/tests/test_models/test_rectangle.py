#!/usr/bin/python3
"""
test_reactangle.py

Performs unit tests for the Reactangle Class.
"""

import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rect = Rectangle(3, 4, 1, 2, 5)

    def test_init(self):
        self.assertEqual(self.rect.width, 3)
        self.assertEqual(self.rect.height, 4)
        self.assertEqual(self.rect.x, 1)
        self.assertEqual(self.rect.y, 2)
        self.assertEqual(self.rect.id, 5)

    def test_width(self):
        self.rect.width = 6
        self.assertEqual(self.rect.width, 6)
        with self.assertRaises(TypeError):
            self.rect.width = "string"
        with self.assertRaises(ValueError):
            self.rect.width = 0

    def test_height(self):
        self.rect.height = 5
        self.assertEqual(self.rect.height, 5)
        with self.assertRaises(TypeError):
            self.rect.height = "string"
        with self.assertRaises(ValueError):
            self.rect.height = -1

    def test_x(self):
        self.rect.x = 3
        self.assertEqual(self.rect.x, 3)
        with self.assertRaises(TypeError):
            self.rect.x = "string"
        with self.assertRaises(ValueError):
            self.rect.x = -1

    def test_y(self):
        self.rect.y = 4
        self.assertEqual(self.rect.y, 4)
        with self.assertRaises(TypeError):
            self.rect.y = "string"
        with self.assertRaises(ValueError):
            self.rect.y = -1

    def test_area(self):
        self.assertEqual(self.rect.area(), 12)

    def test_display(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.rect.display()
            self.assertEqual(fake_out.getvalue(), "\n\n ###\n ###\n ###\n ###\n")

    def test_update(self):
        self.rect.update(2, 5, 6, 7, 8)
        self.assertEqual(self.rect.id, 2)
        self.assertEqual(self.rect.width, 5)
        self.assertEqual(self.rect.height, 6)
        self.assertEqual(self.rect.x, 7)
        self.assertEqual(self.rect.y, 8)

    def test_to_dictionary(self):
        d = {'id': 5, 'width': 3, 'height': 4, 'x': 1, 'y': 2}
        self.assertEqual(self.rect.to_dictionary(), d)
