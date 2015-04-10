#!/usr/bin/env python3


def next_sparse(sparse_number):
    """return next larger sparse number

    Keyword arguments:
        sparse_number -- a sparse number, as defined by is_sparse
        This algorithm uses powers of two. Estimated time complexity >= O(log(n)).
    """

    # print("sparse_number 0b{0:b}".format(sparse_number))

    # Edge case. Handle explicitly for clarity
    if sparse_number == 0:
        return 1

    power_max = twos_power_max(sparse_number)

    for power in range(0, power_max):
        # print("power", power)
        if is_zero_bit_and_no_neighbor_ones(sparse_number, power):
            # print("at middle of 000 change to 010")
            return sparse_number + (2 ** power)
        if is_right_end_of_001(sparse_number, power):
            # print("at right of 001 change to 01 followed by all zeros")
            sparse_zeroed_low_bits = (sparse_number >> (power + 1)) * (2 ** (power + 1))
            # print("sparse_zeroed_low_bits {0:b}".format(sparse_zeroed_low_bits))
            return sparse_zeroed_low_bits + (2 ** (power + 1))

    return (2 ** (power_max + 1))


def next_sparse_incremental(sparse_number):
    """return next larger sparse number

    Keyword arguments:
        sparse_number -- a sparse number, as defined by is_sparse

    return None if reached internal limit without finding a next sparse.

    This algorithm uses "brute force". Estimated time complexity >= O(n).
    Increments until possible_sparse is_sparse or reaches limit.
    """


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
    if exponent > (len(bits) - 1):
        return 0
    else:
        return bits[exponent]


def twos_power_max(number):
    """return highest power of two in number

    Keyword arguments:
        number -- an integer >= 0
    """

    bits = bits_list(number)
    return len(bits) - 1


def is_zero_bit_and_no_neighbor_ones(number, exponent):
    if (bit_at_twos_power(number, exponent) == 0
            and is_bit_no_neighbor_ones(number, exponent)):
        return True
    else:
        return False


def is_bit_no_neighbor_ones(number, exponent):
    if (is_bit_no_right_one(number, exponent)
            and is_bit_no_left_one(number, exponent)):
        return True
    else:
        return False


def is_bit_no_right_one(number, exponent):
    if (exponent == 0
            or bit_at_twos_power(number, exponent - 1) == 0):
        return True
    else:
        return False


def is_bit_no_left_one(number, exponent):
    if bit_at_twos_power(number, exponent + 1) == 0:
        return True
    else:
        return False


def is_right_end_of_001(number, exponent):
    if (bit_at_twos_power(number, exponent) == 1
            and bit_at_twos_power(number, exponent + 1) == 0
            and bit_at_twos_power(number, exponent + 2) == 0):
        return True
    else:
        return False
