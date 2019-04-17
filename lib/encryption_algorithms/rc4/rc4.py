from lib.encryption_algorithms.rc4.utils  import Text, KEY


def encrypt(data, key):

    plain_bytes = data.text_to_bytes()
    key_bytes = key.text_to_bytes()

    key_stream_bytes, encrypted_bytes = crypt(plain_bytes, key_bytes)

    key_stream = Text()
    encrypted = Text()

    key_stream.bytes_to_hex(key_stream_bytes)
    encrypted.bytes_to_hex(encrypted_bytes)

    return key_stream, encrypted.data


def decrypt(data, key):
    encrypted_bytes = data.hex_to_bytes()

    key_bytes = key.text_to_bytes()

    key_stream_bytes, decrypted_bytes = crypt(encrypted_bytes, key_bytes)

    key_stream = Text()
    decrypted = Text()

    key_stream.bytes_to_hex(key_stream_bytes)
    decrypted.bytes_to_text(decrypted_bytes)

    return key_stream, decrypted.data


def crypt(plain_bytes, key_bytes):
    keystream_list = []
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
        keystream_list.append(k)
        cipher_list.append(k ^ plain_bytes[m])

    return keystream_list, cipher_list


def main():

    with open("utils.py", "r") as file:
        data = file.read()

        plain_text = Text(data)
        key = Text(KEY)
        key_stream, encrypted_data = encrypt(plain_text, key)

        encrypted_text = Text(encrypted_data)
        key = Text(KEY)
        key_stream, decrypted = decrypt(encrypted_text, key)
        print(decrypted)


if __name__ == '__main__':
    main()