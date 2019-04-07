import lib.encryption_algorithms.des.constants as constants


def string_to_bits_list(string):
    """
        Turns string into the bits (0 or 1) array

    :param string
    :return: bits array
    """
    string_data = string.encode('ascii')
    array_length = len(string_data) * 8
    result = [0] * array_length

    array_position = 0
    for character in string_data:
        i = 7
        while i >= 0:
            if character & (1 << i) != 0:
                result[array_position] = 1
            else:
                result[array_position] = 0

            array_position += 1
            i -= 1

    return result


def generate_sub_keys(key_string):
    """
        Generates sub keys for Feistel function in DES
    :param key_string: encryption key passed as string
    :return: sub_keys for Feistel function in DES
    """

    bites_key = string_to_bits_list(key_string)

    c_block = [bites_key[constants.permuted_choice_1[i]] for i in range(28)]
    d_block = [bites_key[constants.permuted_choice_1[i + 28]] for i in range(28)]

    sub_keys = []

    i = 0
    while i < 16:

        j = 0
        # Perform circular left shifts
        while j < constants.bits_rotation_table[i]:
            c_block.append(c_block.pop(0))

            d_block.append(d_block.pop(0))

            j += 1

        # Create sub key through pc2 permutation
        c_d_vector = c_block + d_block
        sub_keys.append([c_d_vector[index] for index in constants.permuted_choice_2])

        i += 1

    return sub_keys
