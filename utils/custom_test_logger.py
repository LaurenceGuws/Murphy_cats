import logging
import os
from unittest.runner import TextTestResult, TextTestRunner

# Configure logging
log_dir = 'tests'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Setting up logging to file and console
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# File handler for detailed logging
file_handler = logging.FileHandler(os.path.join(log_dir, 'test_results.log'))
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Console handler for concise logging
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

class CustomTestResult(TextTestResult):
    def addError(self, test, err):
        super().addError(test, err)
        logging.error(f"ERROR: {test} - {err}")
        logging.info(f"ERROR: {self.getDescription(test)} - STATUS CODE: {getattr(test, 'status_code', 'No status code available')}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        logging.error(f"FAIL: {test} - {err}")
        logging.info(f"FAIL: {self.getDescription(test)} - STATUS CODE: {getattr(test, 'status_code', 'No status code available')}")

    def addSuccess(self, test):
        super().addSuccess(test)
        logging.info(f"SUCCESS: {self.getDescription(test)} - STATUS CODE: {getattr(test, 'status_code', 'No status code available')}")

    def stopTestRun(self):
        super().stopTestRun()
        summary = self.getSummary()
        logging.info(summary)
        # Write the full log to a file
        with open(os.path.join(log_dir, 'full_test_log.log'), 'w') as f:
            f.write(self.stream.getvalue())

    def getSummary(self):
        result_summary = (f"Ran {self.testsRun} tests with "
                          f"{len(self.failures)} failures and "
                          f"{len(self.errors)} errors.")
        return result_summary

class CustomTestRunner(TextTestRunner):
    def _makeResult(self):
        return CustomTestResult(self.stream, self.descriptions, self.verbosity)
