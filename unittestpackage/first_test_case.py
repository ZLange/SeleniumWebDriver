import unittest


class TestCaseDemo(unittest.TestCase):  # inherit test class to access all functions

    def setUp(self):
        print("Run once before every test")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):  # clean up setup after test cases are finished
        print("Run after every test")


if __name__ == "__main__":
    unittest.main(verbosity=2)
