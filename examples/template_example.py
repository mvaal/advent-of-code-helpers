import os

from aoc import template
from aoc.helpers import input_lines


class Part1(template.Part1):
    def __init__(self, day: int, year: int, input_file: str, output_dir: str):
        super().__init__(day, year, input_file, output_dir)

    def solve(self):
        # Read input
        lines = input_lines(self.input())
        # Do some work here

        # Sample output
        result = ','.join(lines)
        return result


class Part2(template.Part2):
    def __init__(self, day: int, year: int, input_file: str, output_dir: str):
        super().__init__(day, year, input_file, output_dir)

    def solve(self):
        # Read input
        lines = input_lines(self.input())
        # Do some work here

        # Sample output
        result = ','.join(lines)
        return result


def main():
    file_path = os.path.join(os.path.dirname(__file__), 'resources/input.txt')
    Part1(1, 2018, file_path, '../out').output()
    Part2(1, 2018, file_path, '../out').output()


if __name__ == "__main__":
    main()