from base.selenium_driver_helpers import SeleniumDriverHelpers
from traceback import print_stack
from utilities.util import Util


class PageBase(SeleniumDriverHelpers)

    def __init__(self, driver):
        super(PageBase, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def page_title_verify(self, title_verify):
        try:
            title_current = self.get_title()
            return self.util.