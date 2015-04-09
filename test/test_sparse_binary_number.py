#!/usr/bin/env python3

import unittest
import sparse_binary_number


class TestSparseBinaryNumber(unittest.TestCase):

    """
    sparse number sequence
    000000
    000001
    000010
    000100
    000101
    001000
    001001
    001010
    010000
    010001
    010010
    010100
    010101
    100000
    100001
    100010
    100100
    100101
    101000
    101001
    ...
    """

    def setUp(self):
        self.sparse_numbers = [
            0,
            0b1,
            0b10,
            0b100,
            0b101,
            0b1000,
            0b1001,
            0b1010,
            0b10000,
            0b10001,
            0b10010,
            0b10100,
            0b10101,
            0b100000,
            0b100001,
            0b100010,
            0b100100,
            0b100101,
            0b101000,
            0b101001,
            0b101010
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
        self.assertEqual(0, sparse_binary_number.bit_at_twos_power(number, 2))

    ###############################

    def sequence_two_power(self, exponent):
        """return sequence of bit at exponent in sparse number sequence
        """

        sequence = []
        for number in self.sparse_numbers:
            bit = sparse_binary_number.bit_at_twos_power(number, exponent)
            sequence.append(bit)
        return sequence

    # examine sparse number sequence
    # to help formulate a sparse number generator algorithm

    def test_sequence_two_power0(self):
        sequence = self.sequence_two_power(0)
        expected = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
        self.assertEqual(expected, sequence)

    def test_sequence_two_power1(self):
        sequence = self.sequence_two_power(1)
        expected = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
        self.assertEqual(expected, sequence)

    def test_sequence_two_power2(self):
        sequence = self.sequence_two_power(2)
        expected = [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0]
        self.assertEqual(expected, sequence)

    def test_sequence_two_power3(self):
        sequence = self.sequence_two_power(3)
        expected = [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
        self.assertEqual(expected, sequence)

    def test_sequence_two_power4(self):
        sequence = self.sequence_two_power(4)
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected, sequence)

    def test_sequence_two_power5(self):
        sequence = self.sequence_two_power(5)
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(expected, sequence)

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
            expected = self.sparse_numbers[index]
            self.assertEqual(expected, sparse_binary_number.next_sparse(number),
                             "expected {0} for number 0b{1:b}"
                             .format(str(expected), number))

    def test_next_sparse_limit_returns_none(self):
        test_data = [
            (2 ** 32 - 1, None),
            (2 ** 32, None),
            (2 ** 32 + 1, None)
        ]
        for (number, expected) in test_data:
            self.assertEqual(expected, sparse_binary_number.next_sparse(number),
                             "expected {0} for number 0b{1:b}"
                             .format(str(expected), number))


if __name__ == "__main__":
    unittest.main()
