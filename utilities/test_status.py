import logging
import utilities.custom_logger as cust_log
from base.selenium_driver_helpers import SeleniumDriverHelpers


class TestStatus(SeleniumDriverHelpers):
    log = cust_log.custom_logger(log_level=logging.DEBUG)[0]

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.resultList = []
