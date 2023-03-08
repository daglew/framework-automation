from base.page_base import PageBase
import logging
import utilities.custom_logger as cust_log


class RegisterTestsCourses(PageBase):
    log = cust_log.custom_logger(log_level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.page = self.driver.get("https://courses.letskodeit.com")


"""
Locators
"""
sign_in_button_id = "navbar-inverse-collapse"
password_button_id = "password"
login_button_id = "login"


