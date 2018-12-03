import os
import pathlib


def read_input_from_file(file_path):
    r""" Reads data from file path as a string.

    :param file_path: file path
    :type file_path: str
    :return: data
    :rtype: str
    """
    with open(file_path) as file:
        return file.read()


def input_lines(puzzle_input):
    return puzzle_input.split("\n")


def output(result, part, day, year, output_dir=None):
    print(result)
    if output_dir:
        output_file_dir = os.path.join(output_dir, str(year), str(day))
        pathlib.Path(output_file_dir).mkdir(parents=True, exist_ok=True)
        output_file_path = os.path.join(output_file_dir,
                                        '{}.txt'.format(str(part)))
        with open(output_file_path, "a+") as output_file:
            output_file.write('{}\n'.format(result))
