from lib.encryption_algorithms.rc4.utils  import Text



def main(name, Filename, Action, KeyName='key.txt', *args):

    with open("utils.py", "r") as file:
        data = file.read()
        encrypted = encrypt(data, n)

        d = decrypt(encrypted, p, q)
        print(utils.int_array_to_string(d))

    with open("utils.py", "r") as file:
        data = file.read()
        encrypted = encrypt(data, key)

        d = decrypt(encrypted, key)
        print(d)


if __name__ == '__main__':
    main()