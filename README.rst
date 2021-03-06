Advent of Code helpers
======================

.. image:: https://img.shields.io/pypi/pyversions/advent-of-code-helpers.svg
    :target: https://github.com/mvaal/advent-of-code-helpers
.. image:: https://badge.fury.io/py/advent-of-code-helpers.svg
    :target: https://badge.fury.io/py/advent-of-code-helpers
.. image:: https://github.com/mvaal/advent-of-code-helpers/workflows/build/badge.svg
    :target: https://github.com/mvaal/advent-of-code-helpers
.. image:: https://codecov.io/gh/mvaal/advent-of-code-helpers/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/mvaal/advent-of-code-helpers
.. image:: https://api.codeclimate.com/v1/badges/29103862e179077a63fc/maintainability
    :target: https://codeclimate.com/github/mvaal/advent-of-code-helpers/maintainability
    :alt: Maintainability

Advent of Code helper functions

.. code-block:: python

   from aoc.helpers import output, read_input_from_file, input_lines
   from aoc import template

Setup Guide
-----------

Install with pip

.. code-block:: bash

   pip install advent-of-code-helpers

Helper Usage
------------
``read_input_from_file`` reads the data as a single line from a file

.. code-block:: python

    from aoc.helpers import read_input_from_file
    read_input_from_file('path/to/input_data')

``input_lines`` returns a list of strings from the string input

.. code-block:: python

    from aoc.helpers import input_lines
    input_lines('single\nstring\ninput')

``output`` prints the result to console and writes to an output file if
an output directory is provided

.. code-block:: python

    from aoc.helpers import output
    output('result', part(int), day(int), year(int), output_dir(str), file_prefix(str))

Template Usage
--------------
You can specify data from a file using the ``data(input)`` function.

You can specify an output directory for output using the ``output(output)``
function.  If left empty, it will still print to screen, but will not write
the result to a file.  If given an output directory, the results will be
appended to the file so you can easily go back and look at previous results.

Examples
~~~~~~~~
.. code-block:: python

    from aoc import template


    class Part1(template.Part1):
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

Template Usage with Other Libraries
-----------------------------------
If you want to use your own input reader or a library like advent-of-code-data_,
you can override the ``input`` method.

.. _advent-of-code-data: https://github.com/wimglenn/advent-of-code-data

Examples
~~~~~~~~
.. code-block:: python

    from aoc import template
    from aoc.helpers import input_lines
    from aocd import get_data


    class Part1(template.Part1):
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
        Part1(1, 2018).output('../out')


    if __name__ == "__main__":
        main()
