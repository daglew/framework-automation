import logging
import utilities.custom_logger as cust_log
from base.selenium_driver_helpers import SeleniumDriverHelpers
from traceback import print_stack


class TestStatus(SeleniumDriverHelpers):
    log = cust_log.custom_logger(log_level=logging.DEBUG)[0]

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.result_list = []

    def result_set(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info(f"### SUCCESSFUL CHECK ::  {result_message}")
                else:
                    self.result_list.append("FAIL")
                    self.log.error(f"### FAIL CHECK ::  {result_message}")
                    self.screen_shot(result_message)
            else:
                self.result_list.append("FAIL")
                self.log.error(f"### FAIL CHECK ::  {result_message}")
                self.screen_shot(result_message)

        except:
            self.result_list.append("FAIL")
            self.log.error("### EXCEPTION !!!!!")
            self.screen_shot(result_message)
            print_stack()

    def mark(self, result, result_message):
        self.result_set(result, result_message)

    def final_mark(self, test_name, result, result_message):
        self.result_set(result, result_message)
        if "FAIL" in self.result_list:
            self.log.error(f"{test_name} ### TEST FAILED !")
            self.result_list.clear()
            assert result, f"Result: {result} is not True"
        else:
            self.log.info(f"### TEST SUCCESSFUL ::  {result_message}")
            self.result_list.clear()
            assert result, f"Result: {result} is True"

