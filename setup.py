from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    readme = fh.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

install_requires = []

test_requires = ['pytest>=3']

setup(
    name="advent-of-code-helpers",
    use_scm_version={
        'write_to': 'aoc/version.py',
        'write_to_template': '__version__ = "{version}"\n',
        'tag_regex': r'^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$',
    },
    setup_requires=['setuptools_scm'],
    author="Marcus Vaal",
    license="MIT",
    description="Advent of Code helper functions",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/x-rst",
    url="https://github.com/mvaal/advent-of-code-helpers",
    packages=find_packages(
        exclude=["*.test", "*.test.*", "test.*", "test", ".github"]
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries"
    ],
    install_requires=install_requires,
    tests_require=test_requires
)
