import unittest


def execute_lab6():
    test_suite = unittest.TestLoader().loadTestsFromName('test_calc.TestCalculator')
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)


if __name__ == '__main__':
    execute_lab6()