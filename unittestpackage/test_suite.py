import unittest
from unittestpackage.test_class1 import TestClass1
from unittestpackage.test_class2 import TestClass2

# get all tests
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

# create test suite of combination from test cases
smokeTest = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(smokeTest)