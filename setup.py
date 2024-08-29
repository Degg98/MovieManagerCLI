from setuptools import setup
"""
Setup script for MovieManagerCLI package.

This script is used to install the MovieManagerCLI package and its dependencies.

Attributes:
    name (str): The name of the package.
    version (str): The version of the package.
    py_modules (list): A list of Python modules to include in the package.
    install_requires (list): A list of required packages for installation.
    entry_points (str): A string specifying the console script entry point.

"""

setup(
    name='MovieManagerCLI',
    version='1.0',
    py_modules=['cli'],
    install_requires=[
        'click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        moviemanager=cli:cli
    ''',
)