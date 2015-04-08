#!/usr/bin/env python3

import unittest
import sparse_binary_number


class TestSparseBinaryNumber(unittest.TestCase):

    def setUp(self):
        pass

    def test_bits_0(self):
        self.assertEqual([0], sparse_binary_number.bits(0))

    def test_bits_1(self):
        self.assertEqual([1], sparse_binary_number.bits(0b1))

    def test_bits_3(self):
        self.assertEqual([1, 1], sparse_binary_number.bits(0b11))

    def test_bits_111000101101(self):
        self.assertEqual([1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
                         sparse_binary_number.bits(0b111000101101))

    def test_is_sparse_0(self):
        self.assertEqual(True, sparse_binary_number.is_sparse(0))

    def test_is_sparse_0b1(self):
        self.assertEqual(True, sparse_binary_number.is_sparse(0b1))

    def test_is_sparse_trailing_ones(self):
        self.assertEqual(False, sparse_binary_number.is_sparse(0b000011))

    def test_is_sparse_middle_ones(self):
        self.assertEqual(False, sparse_binary_number.is_sparse(0b001100))

    def test_is_sparse_leading_ones(self):
        self.assertEqual(False, sparse_binary_number.is_sparse(0b110000))

    def test_is_sparse(self):
        test_data = [
            (0, True),
            (0b1, True),
            (0b10, True),
            (0b11, False),
            (0b100, True),
            (0b101, True),
            (5, True),
            (0b110, False),
            (0b1010010010001010001, True),
            (0b1100010010001010001, False)
        ]
        for (number, expected) in test_data:
            self.assertEqual(expected, sparse_binary_number.is_sparse(number),
                             "expected {0} for number 0b{1:b}"
                             .format(str(expected), number))


if __name__ == "__main__":
    unittest.main()
