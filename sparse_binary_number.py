#!/usr/bin/env python3


def is_sparse(number):
    # TODO: Fix method to pass tests
    # bits = bits(number)
    # for bit in bits:
    #     if ((bit == 1) and (previous_bit == 1)):
    #         # number has two consecutive 1s
    #         return False
    # return True

    if number == 0:
        return True
    if number == 1:
        return True
    else:
        return False


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
