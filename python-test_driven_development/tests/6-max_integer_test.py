#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for the max_integer function"""

    def test_ordered_list(self):
        """Test with a sorted list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unsorted list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a list of positive and negative integers"""
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)

    def test_equal_elements(self):
        """Test with a list where all elements are equal"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_non_integer_elements(self):
        """Test with a list containing non-integer elements"""
        with self.assertRaises(TypeError):
            max_integer(["a", 2, 3])

    def test_non_list_argument(self):
        """Test when the argument is not a list"""
        with self.assertRaises(TypeError):
            max_integer(42)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 3.1, 2.0]), 3.1)


if __name__ == "__main__":
    unittest.main()
