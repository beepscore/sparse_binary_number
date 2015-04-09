#!/usr/bin/env python3


def next_sparse(sparse_number):
    """return next larger sparse number

    Keyword arguments:
        sparse_number -- a sparse number, as defined by is_sparse

    return None if reached internal limit without finding a next sparse.
    """

    # increment until possible_sparse is_sparse or reach limit.
    # This algorithm uses "brute force".
    # TODO: make algorithm more efficient

    # limit is arbitrary in Python
    # http://stackoverflow.com/questions/5470693/python-number-limit
    limit = 2 ** 32
    for possible_sparse in range(sparse_number + 1, limit):
        if is_sparse(possible_sparse):
            return possible_sparse
    return None


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


def bit_at_twos_power(number, exponent):
    """return bit in number at location 2 ** exponent

    Keyword arguments:
        number -- an integer >= 0
        exponent -- a integer >= 0
    """

    bits = bits_list(number)
    # NOTE: reverse() modifies object, returns None
    bits.reverse()
    bit = bits[exponent]
    return bit
