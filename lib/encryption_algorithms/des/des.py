from lib.encryption_algorithms.des.utils import crypt, ENCRYPT, DECRYPT


def encrypt(data, key):
    """
        Encrypts passed data with passed key

    :param data: data to encrypt
    :param key: key to encrypt with
    :return: encrypted data as bytes
    """
    return crypt(data, ENCRYPT, key)


def decrypt(encrypted_data, key):
    """
        Decrypts passed data with passed key

    :param encrypted_data: data to decrypt
    :param key: key to decrypt with
    :return: decrypted data as bytes
    """
    return crypt(encrypted_data, DECRYPT, key)


if __name__ == "__main__":
    key = "ASDFGHJK"

    with open("utils.py", "r") as file:
        data = file.read()
        encrypted = encrypt(data, key)

        d = decrypt(encrypted, key)
        print(d)
