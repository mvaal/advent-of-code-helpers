def read_file(file_path):
    r""" Reads data from file path as a string.

    :param file_path: file path
    :type file_path: str
    :return: data
    :rtype: str
    """
    with open(file_path) as file:
        return file.read()
