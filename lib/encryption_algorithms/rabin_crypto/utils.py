import math
import numpy as np


PADDING_BYTES = 'paddingbytes'


def is_prime(n):
    """
        Checks if the passed number is prime

    :param n: number to check
    :return: bool if the number is prime
    """

    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def pow_number_with_mod(number, m):
    """
        Raises to a power number with passed mod

    :param number: number to raise
    :param m: mod
    :return: the operation result
    """

    return pow(number, (m + 1) // 4, m)


def extended_euclid_algorithm(a, b):
    """
        Solves the extended euclid equations

    :param a: the first number
    :param b: the second number
    :return: the unknowns of the equation
    """

    x0, x1 = 1, 0
    y0, y1 = 0, 1

    while b:
        q = a // b

        a, b = b, a % b

        x0, x1 = x1, x0 - x1 * q
        y0, y1 = y1, y0 - y1 * q

    return x0, y0


def add_padding_to_byte(byte):
    """
        Adds padding to byte to find the correct answer later

    :param byte: byte to add padding to
    :return: byte with padding
    """

    binary_str = bin(byte)
    binary_str += bin(int(np.mean([ord(ch) for ch in PADDING_BYTES])))[2:]

    return int(binary_str, 2)


def get_correct_byte_from_variants(variants):
    """
        Returns the correct byte from passed variants.
        The correct variant is retrieved with padding

    :param variants: variants to search from
    :return: the correct result or ? if the result wasn't found
    """
    possible_variants = []

    for i in variants:
        binary = bin(i)
        padding = bin(int(np.mean([ord(ch) for ch in PADDING_BYTES])))[2:]

        if binary[-len(padding):] == padding:
            possible_variants.append(int(binary[:-len(padding)], 2))

    if len(possible_variants) == 0:
        return ord('?')

    return min(possible_variants)


def int_array_to_string(array):
    """
        Turns int array into a string

    :param array: int array
    :return: string
    """
    return bytes(array).decode("utf8")
