from base.selenium_driver_helpers import SeleniumDriverHelpers
from traceback import print_stack
from utilities.util import Util


class PageBase(SeleniumDriverHelpers):

    def __init__(self, driver):
        super(PageBase, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def page_title_verify(self, title_verify):
        try:
            actual_text = self.get_title()
            return self.util.include_verify_text(actual_text, title_verify)
        except:
            self.log.error("Failed to fetch page title.")
            print_stack()
            return False
