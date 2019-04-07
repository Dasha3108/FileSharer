import lib.encryption_algorithms.des.utils as utils


def encrypt(data, key):
    return utils.crypt(data, utils.ENCRYPT, key)


def decrypt(encrypted_data, key):
    return utils.crypt(encrypted_data, utils.DECRYPT, key)


if __name__ == "__main__":
    data = "DES encryption algorithm".encode('ascii')
    key = "DESCRYPT"

    encrypted = encrypt(data, key)
    print(encrypted)
    print(decrypt(encrypted, key))
