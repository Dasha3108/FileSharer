from lib.encryption_algorithms.des.utils import crypt, ENCRYPT, DECRYPT


def encrypt(data, key):
    return crypt(data, ENCRYPT, key)


def decrypt(encrypted_data, key):
    return crypt(encrypted_data, DECRYPT, key)
