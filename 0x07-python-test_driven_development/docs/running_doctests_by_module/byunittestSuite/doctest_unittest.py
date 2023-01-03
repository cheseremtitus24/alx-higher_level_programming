import doctest
import unittest
import module


suite = unittest.TestSuite()
suite.addTest(doctest.DocTestSuite(module))
suite.addTest(doctest.DocFileSuite('doctest_in_help.txt'))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)

