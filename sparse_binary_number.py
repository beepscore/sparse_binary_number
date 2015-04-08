#!/usr/bin/env python3


def next_sparse(sparse_number):
    """return next larger sparse number

    Keyword arguments:
        sparse_number -- a sparse number, as defined by is_sparse
    """

    # TODO: generalize method
    return 5


def is_sparse(number):
    """return True if number binary digit 1s have no adjacent 1s.

    Keyword arguments:
        number -- an integer >= 0

    return True if number is 0b1
    """

    if number == 0:
        return True
    if number == 1:
        # edge case. List explicitly for clarity. Define to be True
        return True
    else:
        bits = bits_list(number)
        # start power_of_2 at 1 so previous_bit index won't be out of list range
        for power_of_2 in range(1, len(bits)):
            current_bit = bits[power_of_2]
            previous_bit = bits[power_of_2 - 1]
            if ((current_bit == 1) and (previous_bit == 1)):
                # number has two consecutive 1s
                return False
        return True


def bits_list(number):
    """return list of bits in number

    Keyword arguments:
        number -- an integer >= 0
    """

    # https://wiki.python.org/moin/BitManipulation
    if number == 0:
        return [0]
    else:
        # binary_literal string e.g. '0b101'
        binary_literal = bin(number)
        bits_string = binary_literal.lstrip('0b')
        # list comprehension
        bits = [int(bit_character) for bit_character in bits_string]
        return bits
