import os
import sys

if sys.version_info >= (3, 5):
    import pathlib
else:
    import errno


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

    def mkdir_p(path):
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

    if output_dir:
        output_file_dir = os.path.join(output_dir, str(year), str(day))
        if sys.version_info >= (3, 5):
            pathlib.Path(output_file_dir).mkdir(parents=True, exist_ok=True)
        else:
            mkdir_p(output_file_dir)
        output_file_path = os.path.join(output_file_dir,
                                        '{}.txt'.format(str(part)))
        with open(output_file_path, "a+") as output_file:
            output_file.write('{}\n'.format(result))
