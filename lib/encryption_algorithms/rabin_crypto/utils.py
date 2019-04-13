import math
import numpy as np


PADDING_BYTES = 'paddingbytes'


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def pow_number_with_mod(number, m):
    return pow(number, (m + 1) // 4, m)


def extended_euclid_algorithm(a, b):
    x0, x1 = 1, 0
    y0, y1 = 0, 1

    while b:
        q = a // b

        a, b = b, a % b

        x0, x1 = x1, x0 - x1 * q
        y0, y1 = y1, y0 - y1 * q

    return x0, y0


def add_padding_to_byte(byte):
    binary_str = bin(byte)
    binary_str += bin(int(np.mean([ord(ch) for ch in PADDING_BYTES])))[2:]

    return int(binary_str, 2)


def get_correct_byte_from_variants(variants):
    possible_variants = []

    for i in variants:
        binary = bin(i)
        padding = bin(int(np.mean([ord(ch) for ch in PADDING_BYTES])))[2:]

        if binary[-len(padding):] == padding:
            possible_variants.append(int(binary[:-len(padding)], 2))

    if len(possible_variants) == 0:
        return ord('?')

    return min(possible_variants)