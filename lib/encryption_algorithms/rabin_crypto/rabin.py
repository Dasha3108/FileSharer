import lib.encryption_algorithms.rabin_crypto.utils as utils
import random


def generate_keys():
    prime_numbers = [i for i in range(1000, 10000) if utils.is_prime(i) and i % 4 == 3]

    p = random.choice(prime_numbers)
    q = random.choice(prime_numbers)

    n = p * q

    return p, q, n


def encrypt(data, n):
    encrypted_data = []
    a = []
    for byte in data:
        byte_with_padding = utils.add_padding_to_byte(byte)
        a.append(byte)
        encrypted_data.append((byte_with_padding * byte_with_padding) % n)

    print(a)
    return encrypted_data


def decrypt(encrypted_data, p, q):
    n = p * q

    decrypted_data = []
    for encrypted_byte in encrypted_data:
        m_p = utils.pow_number_with_mod(encrypted_byte, p)
        m_q = utils.pow_number_with_mod(encrypted_byte, q)

        y_p, y_q = utils.extended_euclid_algorithm(p, q)

        x = (y_p * p * m_q + y_q * q * m_p) % n
        y = (y_p * p * m_q - y_q * q * m_p) % n

        variants = [x, n - x, y, n - y]
        decrypted_data.append(utils.get_correct_byte_from_variants(variants))

    return decrypted_data


if __name__ == "__main__":
    p, q, n = generate_keys()

    with open("utils.py", "rb") as file:
        data = file.read()
        encrypted = encrypt(data, n)

        print(decrypt(encrypted, p, q))

    print(p, q, n)

