# tests/runner.py
import unittest

# import your test modules
import unittestExample
import Scrape_Test
import Scrape_Test_Weather
import Test_temp

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(unittestExample))
suite.addTests(loader.loadTestsFromModule(Scrape_Test))
suite.addTests(loader.loadTestsFromModule(Scrape_Test_Weather))
suite.addTests(loader.loadTestsFromModule(Test_temp))


# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)