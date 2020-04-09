import setuptools

with open("README.rst", "r") as fh:
    readme = fh.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

install_requires = []

test_requirements = ['pytest>=3']

setuptools.setup(
    name="advent-of-code-helpers",
    version="0.1.1",
    author="Marcus Vaal",
    license="MIT",
    description="Advent of Code helper functions",
    long_description= readme + '\n\n' + history,
    long_description_content_type="text/x-rst",
    url="https://github.com/mvaal/advent-of-code-helpers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries"
    ],
    install_requires=install_requires,
    test_requirements=test_requirements
)
