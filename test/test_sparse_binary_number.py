#!/usr/bin/env python3

import unittest
import sparse_binary_number


class TestSparseBinaryNumber(unittest.TestCase):

    def setUp(self):
        pass

    def test_is_sparse_0(self):
        self.assertEqual(True, sparse_binary_number.is_sparse(0))

    def test_is_sparse_0b1(self):
        self.assertEqual(True, sparse_binary_number.is_sparse(0b1))

    def test_is_sparse_0b10(self):
        self.assertEqual(True, sparse_binary_number.is_sparse(0b10))

    def test_is_sparse_0b11(self):
        self.assertEqual(False, sparse_binary_number.is_sparse(0b11))

    # TODO: Consider change test data to a list of tuples
    # test_data = [(0, True), (1, True), (2, True), (3, False) ]


if __name__ == "__main__":
    unittest.main()
