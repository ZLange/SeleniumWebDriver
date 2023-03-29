"""
in order to generate test report run command -> pytest -s -v .\test_reporting.py --html=htmlreport.html
in the end adding file name or location where the file should be crated

"""

import pytest
import sys

sys.path.insert(0, "C:\\Users\\zozol\\PycharmProjects\\SeleniumWebDriver\\advancedTestingFramework")
"""
in order to run these tests add sys import for path:

import sys

sys.path.insert(0, "here path to folder where needed method file is")

"""
from class_to_test import SomeTestClass


@pytest.mark.usefixtures("onetimesetup", "setup")
class TestReport:

    @pytest.fixture(autouse=True)  # makes available for all scope
    def classsetup(self):
        self.abc = SomeTestClass(self.value)

    def test_a(self):
        result = self.abc.sum_num(2, 8)
        assert result == 20
        print("running case A")

    def test_b(self):
        result = self.abc.sum_num(2, 8)
        assert result > 20
        print("running case B")
