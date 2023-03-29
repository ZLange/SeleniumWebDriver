import pytest


@pytest.fixture()
def setup():
    print("Once before every method")
    yield  # needed to run the same in the end of tests
    print("Once after every method")


def test_method2_a(setup):
    print("Running method2 A")


def test_method2_b(setup):
    print("Running method2 B")

# for running specific test file  -> pytest -s .\test_case_demo2.py
