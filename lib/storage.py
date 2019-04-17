import os

FILES_FOLDER = 'uploaded_files/'

CLIENT_FOLDER = 'downloaded_files/'


def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        directory_path = os.path.join(os.path.curdir, directory)

        os.makedirs(directory_path)


def save_data_to_file_in_storage(data, file_name):
    create_directory_if_not_exists(FILES_FOLDER)

    file_path = os.path.join(os.path.curdir, FILES_FOLDER, file_name)

    with open(file_path, "wb") as file:
        file.write(data)


def save_data_to_file_in_client_storage(data, file_name):
    create_directory_if_not_exists(CLIENT_FOLDER)

    file_path = os.path.join(os.path.curdir, CLIENT_FOLDER, file_name)

    with open(file_path, "wb") as file:
        file.write(data)


def get_data_from_file_in_storage(file_name):
    file_path = os.path.join(os.path.curdir, FILES_FOLDER, file_name)

    if not os.path.exists(file_path):
        return None

    with open(file_path, "r") as file:
        data = file.read()

    return data


def get_all_files_names_in_storage():
    location = os.path.join(os.path.curdir, FILES_FOLDER)

    return [file for file in os.listdir(location) if os.path.isfile(os.path.join(location, file))]