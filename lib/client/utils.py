import os


KEY = "Secret"


def create_file(file_name):
    """
        Creates the file with the passed name.
        Deletes the file if it exists and creates a new one
    """
    delete_file(file_name)

    return open(file_name, 'a+')


def get_data_from_file(file_name):
    """
        Reads and returns the data from the file with the passed name

    :param file_name: the file name from which the data will be retrieved
    :return: the file data if it exists, otherwise returns None
    """

    if not os.path.exists(file_name):
        return None

    file = open(file_name, "r")
    data = file.read()
    file.close()

    return data


def delete_file(file_name):
    """
        Deletes the file if it exists
    """
    try:
        os.remove(file_name)
    except OSError:
        pass
