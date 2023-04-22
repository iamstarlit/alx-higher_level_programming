#!/usr/bin/python3
"""
6-max_integer_test.py

Unit Test script for max_inter(list=[]):
This tests the function using `unnittest` module.
"""

# importing modules
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest sub-class for the max_integer(list=[]) function."""

    def test_sorted(self):
        """Tests a sorted list of int and float."""
        sorted_int = [1, 2, 3, 4]
        sorted_float = [1.1, 2.2, 3.3, 4.4]

        # Test using assertEqual method
        self.assertEqual(max_integer(sorted_int), 4)
        self.assertEqual(max_integer(sorted_float), 4.4)

    def test_unsorted(self):
        """Tests unsorted list of int and float."""
        unsorted_int = [1, 3, 2, 4]
        unsorted_float = [1.2, 3.3, 2.2, 4.4]

        # Test using assertEqual method
        self.assertEqual(max_integer(unsorted_int), 4)
        self.assertEqual(max_integer(unsorted_float), 4.4)

    def test_mixture(self):
        """Tests a mixed list of int and float."""
        mixed_list = [1, 2.2, -3, -4.5]

        # Testing using assertEqual method
        self.assertEqual(max_integer(mixed_list), 2.2)

    def test_strings(self):
        """Tests a list of strings."""
        strings = ["str1", "str2", "str3"]
        repeated_str = ["str1", "str2", "str2"]
        mixed_str = ["Paul", "Asnath", "John"]

        # Testing using assertEqual method
        self.assertEqual(max_integer(strings), 'str3')
        self.assertEqual(max_integer(repeated_str), 'str2')
        self.assertEqual(max_integer(mixed_str), 'Paul')

    def test_empty(self):
        empty_list = []

        # Testing using assertEqual method
        self.assertEqual(max_integer(empty_list), None)

    def test_mono(self):
        """Tests a list with one element."""
        mono_list_1 = [1]
        mono_list_2 = ["Asnath"]

        # Testing using assertEqual method
        self.assertEqual(max_integer(mono_list_1), 1)
        self.assertEqual(max_integer(mono_list_2), 'Asnath')


if __name__ == "__main__":
    unittest.main()
