from lib.encryption_algorithms.rc4.utils import Text, KEY


def encrypt(data, key):
    data = Text(data)
    key = Text(key)

    plain_bytes = data.text_to_bytes()
    key_bytes = key.text_to_bytes()

    encrypted_bytes = crypt(plain_bytes, key_bytes)

    encrypted = Text()

    encrypted.bytes_to_hex(encrypted_bytes)

    return encrypted.data


def decrypt(data, key):
    data = Text(data)
    key = Text(key)

    encrypted_bytes = data.hex_to_bytes()

    key_bytes = key.text_to_bytes()

    decrypted_bytes = crypt(encrypted_bytes, key_bytes)

    decrypted = Text()

    decrypted.bytes_to_text(decrypted_bytes)

    return decrypted.data


def crypt(plain_bytes, key_bytes):
    key_stream_list = []
    cipher_list = []

    key_len = len(key_bytes)
    plain_len = len(plain_bytes)
    S = list(range(256))

    j = 0
    for i in range(256):
        j = (j + S[i] + key_bytes[i % key_len]) % 256

        S[i], S[j] = S[j], S[i]

    i = 0
    j = 0
    for m in range(plain_len):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        key_stream_list.append(k)
        cipher_list.append(k ^ plain_bytes[m])

    return cipher_list


def main():

    with open("file.txt", "r") as file:
        data = file.read()

        encrypted_data = encrypt(data, KEY)

        print encrypted_data

        decrypted = decrypt(encrypted_data, KEY)
        print(decrypted)


if __name__ == '__main__':
    main()