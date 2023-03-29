"""
-s to print statements
-v verbose
-k run specific method from file
"""

import pytest


@pytest.fixture()
def setup():
    print("Once before every method")
    yield  # needed to run the same in the end of tests
    print("Once after every method")


def test_method3_a(setup):
    print("Running method3 A")


def test_method3_b(setup):
    print("Running method3 B")
