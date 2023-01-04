#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    test_val = [1, 2, 3, 4]
    test_val1 = [5, 2, 3, 4]
    test_val2 = [-5, -2, -3, -4]
    test_val3 = [-5, -5, -5, -5]
    test_val4 = [5, 5, 5, 5]
    test_non_integer_vals = ['1', 2, tuple(), list()]

    def test_maxinteger(self):
        # Test for normal output for +ve & -ve numbers
        self.assertAlmostEqual(max_integer(self.__class__.test_val), 4)
        self.assertAlmostEqual(max_integer(self.__class__.test_val1), 5)
        self.assertAlmostEqual(max_integer(self.__class__.test_val2), -2)
        # test when list items are the same value
        self.assertAlmostEqual(max_integer(self.__class__.test_val3), -5)
        self.assertAlmostEqual(max_integer(self.__class__.test_val4), 5)

    def test_value(self):
        # Tests for proper output when empty list is provided
        self.assertAlmostEqual(max_integer(list()), None)

    def test_type_error(self):
        # test when list contains non-integer values
        self.assertRaises(
            TypeError,
            max_integer,
            self.__class__.test_non_integer_vals)
