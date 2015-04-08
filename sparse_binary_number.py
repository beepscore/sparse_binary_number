#!/usr/bin/env python3


def is_sparse(number):
    if number == 0:
        return True
    if number == 1:
        return True
    else:
        bits_list = bits(number)
        # start power_of_2 at 1 so previous_bit index won't be out of list range
        for power_of_2 in range(1, len(bits_list)):
            current_bit = bits_list[power_of_2]
            previous_bit = bits_list[power_of_2 - 1]
            if ((current_bit == 1) and (previous_bit == 1)):
                # number has two consecutive 1s
                return False
        return True


def bits(number):
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
