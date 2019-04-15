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


def crypt(PlainBytes, KeyBytes):

    keystreamList = []
    cipherList = []

    keyLen = len(KeyBytes)
    plainLen = len(PlainBytes)
    S = list(range(256))

    j = 0
    for i in range(256):
        j = (j + S[i] + KeyBytes[i % keyLen]) % 256

        S[i], S[j] = S[j], S[i]

    i = 0
    j = 0
    for m in range(plainLen):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        keystreamList.append(k)
        cipherList.append(k ^ PlainBytes[m])

    return keystreamList, cipherList


def main():

    with open("utils.py", "r") as file:
        data = file.read()

        #print(data)

        plain_text = Text(data)
        key = Text(KEY)
        key_stream, encrypted_data = encrypt(plain_text, key)

        #print(encrypted_data)

        encrypted_text = Text(encrypted_data)
        key = Text(KEY)
        key_stream, decrypted = decrypt(encrypted_text, key)
        print(decrypted)


if __name__ == '__main__':
    main()