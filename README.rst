Advent of Code helpers
======================
.. image:: https://travis-ci.org/mvaal/advent-of-code-helpers.svg?branch=master
    :target: https://travis-ci.org/mvaal/advent-of-code-helpers
.. image:: https://badge.fury.io/py/advent-of-code-helpers.svg
    :target: https://badge.fury.io/py/advent-of-code-helpers
.. image:: https://coveralls.io/repos/github/mvaal/advent-of-code-helpers/badge.svg
    :target: https://coveralls.io/github/mvaal/advent-of-code-helpers

Advent of Code helper functions

.. code-block:: python

   from aoc.helpers import output, read_input_from_file, input_lines
   from aoc import template

Setup Guide
-----------

Install with pip

.. code-block:: bash

   pip install advent-of-code-helpers

Template Usage
--------------
.. code-block:: python

    from aoc import template


    class Part1(template.Part1):
        def __init__(self, day: int, year: int) -> None:
            super().__init__(day, year)

        def solve(self):
            # Read input
            lines = input_lines(self.input())
            # Do some work here

            # Sample output
            result = ','.join(lines)
            return result


    def main():
        output_dir = '../out'
        test_data = os.path.join(os.path.dirname(__file__),
                                 'resources/test_input.txt')
        Part1(1, 2018).data(test_data).output(output_dir)

        data = os.path.join(os.path.dirname(__file__), 'resources/input.txt')
        Part1(1, 2018).data(data).output(output_dir)


    if __name__ == "__main__":
        main()

More usage in the example_.

.. _example: examples/template_example.py

Template Usage with other libraries
-----------------------------------
If you want to use your own input reader or a library like advent-of-code-data_,
you can override the ``input`` method.

.. _advent-of-code-data: https://github.com/wimglenn/advent-of-code-data

.. code-block:: python

    from aoc import template
    from aoc.helpers import input_lines
    from aocd import get_data


    class Part1(template.Part1):
        def __init__(self, day: int, year: int) -> None:
            super().__init__(day, year)

        def input(self):
            if self.input_file:
                return super().input()
            else:
                return get_data(day=self.day, year=self.year)

        def solve(self):
            # Read input
            lines = input_lines(self.input())
            # Do some work here

            # Sample output
            result = ','.join(lines)
            return result


    def main():
        Part1(2, 2018).output('../out')


    if __name__ == "__main__":
        main()