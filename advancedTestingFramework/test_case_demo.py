import pytest


@pytest.fixture()
def setup():
    print("Once before every method")


def test_method_a(setup):
    print("Running method A")


def test_method_b(setup):
    print("Running method B")

# for running with more details use pytest -v -s
