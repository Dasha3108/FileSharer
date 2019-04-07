import lib.encryption_algorithms.des.constants as constants

ENCRYPT = 0
DECRYPT = 1


def string_to_bits_list(string):
    """
        Turns string into the bits (0 or 1) array

    :param string
    :return: bits array
    """
    string_data = string.encode('ascii')
    return bytes_to_bits_list(string_data)


def bytes_to_bits_list(data):
    """
        Turns bytes into the bits (0 or 1) array

    :param data
    :return: bits array
    """
    array_length = len(data) * 8
    result = [0] * array_length

    array_position = 0
    for character in data:
        i = 7
        while i >= 0:
            if character & (1 << i) != 0:
                result[array_position] = 1
            else:
                result[array_position] = 0

            array_position += 1
            i -= 1

    return result


def bits_list_to_bytes(data):
    """
        Turns the bits (0 or 1) array into bytes

    :param data
    :return: bytes array
    """
    result = []
    position = 0
    c = 0
    while position < len(data):
        c += data[position] << (7 - (position % 8))
        if (position % 8) == 7:
            result.append(c)
            c = 0

        position += 1

    return bytes(result)


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


def crypt(data, crypt_type, key, block_size=8):
    """
        Main DES flow. Separates data in blocks and passes them to DES algorithm.
    :param key: key to crypt data
    :param data: bits array to encrypt
    :param crypt_type: ENCRYPT or DECRYPT
    :param block_size: the size of data blocks
    :return: crypted data
    """

    if len(data) % block_size != 0:
        raise ValueError("Invalid data length, data must be a multiple of " + str(block_size) + " bytes\n")

    if crypt_type == ENCRYPT:
        sub_keys = generate_sub_keys(key)
    else:
        sub_keys = generate_sub_keys(key)
        sub_keys.reverse()

    i = 0
    crypted_data = []
    while i < len(data):
        block = bytes_to_bits_list(data[i:i + block_size])

        crypted_block = des_algorithm(block, sub_keys)

        crypted_data.append(bits_list_to_bytes(crypted_block))

        i += block_size

    return bytes.fromhex('').join(crypted_data)


def des_algorithm(block, sub_keys):
    """
        Crypts block with DES algorithm
    :param sub_keys: keys for des iterations
    :param block: block passed for crypting
    :return: crypted block
    """

    # Initial permutation
    block = [block[index] for index in constants.initial_permutation]

    left_block = block[:32]
    right_block = block[32:]

    i = 0
    while i < 16:
        left_block, right_block = des_algorithm_iteration(left_block, right_block, sub_keys[i])

        i += 1

    # Final permutation
    block = right_block + left_block
    block = [block[index] for index in constants.final_permutation]

    return block


def des_algorithm_iteration(left_block, right_block, iteration_key):
    temp_right_block = right_block[:]

    # Expands right bits from 32 to 64
    right_block = [right_block[index] for index in constants.expansion_function]

    # XOR R[i - 1] with K[i]
    right_block = list(map(lambda x, y: x ^ y, right_block, iteration_key))

    # Separate block into 6 bits blocks to prepare for S-boxes permutation
    six_bits_blocks = [right_block[:6], right_block[6:12], right_block[12:18], right_block[18:24], right_block[24:30],
                       right_block[30:36], right_block[36:42], right_block[42:]]

    # Permutate blocks using the S-Boxes
    j = 0
    position = 0
    while j < 8:
        # Calculate the offsets
        m = (six_bits_blocks[j][0] << 1) + six_bits_blocks[j][5]
        n = (six_bits_blocks[j][1] << 3) + (six_bits_blocks[j][2] << 2) + (six_bits_blocks[j][3]
                                                                           << 1) + six_bits_blocks[j][4]

        # Find the permutation value
        v = constants.s_boxes[j][(m << 4) + n]

        # Turn value into bits
        right_block[position] = (v & 8) >> 3
        right_block[position + 1] = (v & 4) >> 2
        right_block[position + 2] = (v & 2) >> 1
        right_block[position + 3] = v & 1

        position += 4
        j += 1

    # Shuffles the bits of a 32-bit right block
    right_block = [right_block[index] for index in constants.permutation]

    # XOR with L[i - 1]
    right_block = list(map(lambda x, y: x ^ y, right_block, left_block))

    # L[i] = R[i - 1]
    left_block = temp_right_block

    return left_block, right_block
