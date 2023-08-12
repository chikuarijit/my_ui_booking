import unittest


class CustomTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.passed = []
        self.failed = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.passed.append(test)

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.failed.append(test)

    def print_results(self):
        print("Collected", self.testsRun, "test cases.")
        print("Passed:", len(self.passed))
        for test in self.passed:
            print("  [PASSED]", test)

        print("Failed:", len(self.failed))
        for test, err in self.failures:
            print("  [FAILED]", test)
            print("    ", err)


class CustomTestRunner(unittest.TextTestRunner):
    resultclass = CustomTestResult
