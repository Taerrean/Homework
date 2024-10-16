import unittest, tests_12_3

tests = unittest.TestSuite()
tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.Tournament_test))
tests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(tests)
