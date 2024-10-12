"""
Runs the doctests.

Each file/module which contains tests has to be added with the testmod method!
"""

import doctest

import lost_spc.constants


def run_doctests():
    doctest.testmod(lost_spc.constants)


if __name__ == "__main__":
    run_doctests()
