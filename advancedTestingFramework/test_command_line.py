import pytest


def test_command_line_methoda(onetimesetup, setup):
    print("Running method A")


def test_command_line_methodb(onetimesetup, setup):
    print("Running method B")

# to run use command -> pytest -s -v .\test_command_line.py --browser firefox
# used defined commands from conftest
