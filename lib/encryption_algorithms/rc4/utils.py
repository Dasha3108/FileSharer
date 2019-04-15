


class Text:

    def __init__(self, data):
        self.data = data

    def text_to_bytes(self):

        byte_list = []

        for byte in self.data:
            byte_list.append(ord(byte))

        return byte_list

    def hex_to_bytes(self):

        byte_list = []

        for i in range(0, len(self.data), 2):
            byte = self.data[i:i + 2]
            byte_list.append(int('0X' + byte, 16))

        return byte_list

    def bytes_to_text(self, byte_list):

        data = ''
        for byte in byte_list:
            data += chr(byte)

        return data


    def bytes_to_hex(self, byte_list):

        data = ''

        for byte in byte_list:
            hex_str = '0' + hex(byte)[2:]
            data += hex_str[-2:].upper()
