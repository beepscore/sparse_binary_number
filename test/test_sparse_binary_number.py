#!/usr/bin/env python3

import unittest
import sparse_binary_number


class TestSparseBinaryNumber(unittest.TestCase):

    def setUp(self):
        self.sparse_numbers = [
            0b00000000,
            0b00000001,
            0b00000010,
            0b00000100,
            0b00000101,
            0b00001000,
            0b00001001,
            0b00001010,
            0b00010000,
            0b00010001,
            0b00010010,
            0b00010100,
            0b00010101,
            0b00100000,
            0b00100001,
            0b00100010,
            0b00100100,
            0b00100101,
            0b00101000,
            0b00101001,
            0b00101010,
            0b01000000,
            0b01000001,
            0b01000010,
            0b01000100,
            0b01000101,
            0b01001000,
            0b01001001,
            0b01001010,
            0b01010000,
            0b01010001,
            0b01010010,
            0b01010100,
            0b01010101,
            0b10000000
        ]

    def test_bit_at_twos_power(self):
        # expected, number, twos_power
        number = 0b11001101
        self.assertEqual(1, sparse_binary_number.bit_at_twos_power(number, 0))
        self.assertEqual(0, sparse_binary_number.bit_at_twos_power(number, 1))
        self.assertEqual(1, sparse_binary_number.bit_at_twos_power(number, 2))
        self.assertEqual(1, sparse_binary_number.bit_at_twos_power(number, 3))
        self.assertEqual(0, sparse_binary_number.bit_at_twos_power(number, 4))
        self.assertEqual(0, sparse_binary_number.bit_at_twos_power(number, 5))
        self.assertEqual(1, sparse_binary_number.bit_at_twos_power(number, 6))
        self.assertEqual(1, sparse_binary_number.bit_at_twos_power(number, 7))

    def test_bit_at_twos_power_leading_zeros(self):
        # expected, number, twos_power
        number = 0b01
        self.assertEqual(1, sparse_binary_number.bit_at_twos_power(number, 0))
        self.assertEqual(0, sparse_binary_number.bit_at_twos_power(number, 1))

    def test_bit_at_twos_power_higher_than_most_significant_bit(self):
        self.assertEqual(0, sparse_binary_number.bit_at_twos_power(0b01, 8))
        self.assertEqual(0, sparse_binary_number.bit_at_twos_power(0b01, 12))

    ###############################

    # examine sparse number sequence
    # to help formulate a sparse number generator algorithm

    def sequence_difference(self):
        difference_list = []
        for index in range(1, len(self.sparse_numbers)):
            difference = self.sparse_numbers[index]
            - self.sparse_numbers[index - 1]
            difference_list.append(difference)
        return difference_list

    def test_sequence_difference(self):
        difference_list = self.sequence_difference()
        expected = [
            1,
            2,
            4, 5,
            8, 9, 10,
            16, 17, 18, 20, 21,
            32, 33, 34, 36, 37, 40, 41, 42,
            64, 65, 66, 68, 69, 72, 73, 74, 80, 81, 82, 84, 85,
            128
        ]
        self.assertEqual(expected, difference_list)
        # expand elements as powers of 2 to make pattern clearer
        expected_expanded = [
            1,
            2,
            4, 4 + 1,
            8, 8 + 1, 8 + 2,
            16, 16 + 1, 16 + 2, 16 + 4, 16 + 4 + 1,
            32, 32 + 1, 32 + 2, 32 + 4, 32 + 4 + 1,
            32 + 8, 32 + 8 + 1, 32 + 8 + 2,
            64, 64 + 1, 64 + 2, 64 + 4, 64 + 4 + 1,
            64 + 8, 64 + 8 + 1, 64 + 8 + 2,
            64 + 16, 64 + 16 + 1, 64 + 16 + 2, 64 + 16 + 4, 64 + 16 + 4 + 1,
            128
        ]
        self.assertEqual(expected_expanded, difference_list)

    ###############################

    def test_bits_list_0(self):
        self.assertEqual([0], sparse_binary_number.bits_list(0))

    def test_bits_list_1(self):
        self.assertEqual([1], sparse_binary_number.bits_list(0b1))

    def test_bits_list_3(self):
        self.assertEqual([1, 1], sparse_binary_number.bits_list(0b11))

    def test_bits_list_111000101101(self):
        self.assertEqual([1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
                         sparse_binary_number.bits_list(0b111000101101))

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

    def test_next_sparse(self):
        for index in range(1, len(self.sparse_numbers)):
            number = self.sparse_numbers[index - 1]
            actual = sparse_binary_number.next_sparse(number)
            expected = self.sparse_numbers[index]
            self.assertEqual(expected, actual,
                             "expected 0b{0:b} for next_sparse(0b{1:b}) but got 0b{2:b}"
                             .format(expected, number, actual))

    def test_next_sparse_incremental(self):
        for index in range(1, len(self.sparse_numbers)):
            number = self.sparse_numbers[index - 1]
            actual = sparse_binary_number.next_sparse_incremental(number)
            expected = self.sparse_numbers[index]
            self.assertEqual(expected, actual,
                             "expected 0b{0:b} for next_sparse_incremental(0b{1:b}) but got 0b{2:b}"
                             .format(expected, number, actual))

    def test_next_sparse_incremental_limit_returns_none(self):
        test_data = [
            (2 ** 32 - 1, None),
            (2 ** 32, None),
            (2 ** 32 + 1, None)
        ]
        for (number, expected) in test_data:
            actual = sparse_binary_number.next_sparse_incremental(number)
            self.assertEqual(expected, actual,
                             "expected {0} for next_sparse_incremental(0b{1:b})"
                             .format(str(expected), number))

    def test_twos_power_max(self):
        self.assertEqual(0, sparse_binary_number.twos_power_max(0))
        self.assertEqual(0, sparse_binary_number.twos_power_max(0b1))
        self.assertEqual(0, sparse_binary_number.twos_power_max(0b01))
        self.assertEqual(1, sparse_binary_number.twos_power_max(0b10))
        self.assertEqual(1, sparse_binary_number.twos_power_max(0b11))
        self.assertEqual(3, sparse_binary_number.twos_power_max(0b01011))

    def test_is_zero_bit_and_no_neighbor_ones(self):
        self.assertEqual(True,
                         sparse_binary_number.is_zero_bit_and_no_neighbor_ones(0b0, 0))
        self.assertEqual(False,
                         sparse_binary_number.is_zero_bit_and_no_neighbor_ones(0b1, 0))
        self.assertEqual(False,
                         sparse_binary_number.is_zero_bit_and_no_neighbor_ones(0b001, 1))
        self.assertEqual(False,
                         sparse_binary_number.is_zero_bit_and_no_neighbor_ones(0b10, 0))
        self.assertEqual(False,
                         sparse_binary_number.is_zero_bit_and_no_neighbor_ones(0b10, 1))
        self.assertEqual(False,
                         sparse_binary_number.is_zero_bit_and_no_neighbor_ones(0b010, 1))
        self.assertEqual(True,
                         sparse_binary_number.is_zero_bit_and_no_neighbor_ones(0b100, 0))
        self.assertEqual(True,
                         sparse_binary_number.is_zero_bit_and_no_neighbor_ones(0b1010001, 2))

    def test_is_bit_no_neighbor_ones(self):
        self.assertEqual(True,
                         sparse_binary_number.is_bit_no_neighbor_ones(0b0, 0))
        self.assertEqual(True,
                         sparse_binary_number.is_bit_no_neighbor_ones(0b1, 0))
        self.assertEqual(False,
                         sparse_binary_number.is_bit_no_neighbor_ones(0b10, 0))
        self.assertEqual(True,
                         sparse_binary_number.is_bit_no_neighbor_ones(0b10, 1))
        self.assertEqual(True,
                         sparse_binary_number.is_bit_no_neighbor_ones(0b010, 1))
        self.assertEqual(False,
                         sparse_binary_number.is_bit_no_neighbor_ones(0b001, 1))
        self.assertEqual(False,
                         sparse_binary_number.is_bit_no_neighbor_ones(0b100, 1))

    def test_is_bit_no_right_one(self):
        self.assertEqual(True, sparse_binary_number.is_bit_no_right_one(0b0, 0))
        self.assertEqual(True, sparse_binary_number.is_bit_no_right_one(0b1, 0))
        self.assertEqual(False,
                         sparse_binary_number.is_bit_no_right_one(0b01, 1))
        self.assertEqual(True,
                         sparse_binary_number.is_bit_no_right_one(0b10, 1))

    def test_is_bit_no_left_one(self):
        self.assertEqual(True, sparse_binary_number.is_bit_no_left_one(0b0, 0))
        self.assertEqual(True, sparse_binary_number.is_bit_no_left_one(0b1, 0))
        self.assertEqual(False,
                         sparse_binary_number.is_bit_no_left_one(0b10, 0))
        self.assertEqual(True,
                         sparse_binary_number.is_bit_no_left_one(0b10, 1))
        self.assertEqual(True,
                         sparse_binary_number.is_bit_no_left_one(0b11, 1))
        self.assertEqual(False,
                         sparse_binary_number.is_bit_no_left_one(0b101, 1))

if __name__ == "__main__":
    unittest.main()
