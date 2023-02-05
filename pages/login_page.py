import time

from selenium.webdriver.common.by import By
from base.selenium_driver_helpers import SeleniumDriverHelpers
import logging
import utilities.custom_logger as cust_log


class PageLogin(SeleniumDriverHelpers):

    log, file_handler = cust_log.custom_logger(log_level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # loc
    _login_xpath = "//a[@href='/login']"
    _addres_email_xpath = "//input[@id='email' and @class='form-control input-md']"
    _password_id = "password"
    _button_login_xpath = "//button[@id='login']"

    def click_login_link(self):
        self.click_element(self._login_xpath, "xpath")
        # self.get_login().click()

    def email_enter(self, email_address):
        self.send_the_keys(email_address, self._addres_email_xpath, locator_type="xpath")
        # self.get_login().send_keys(email)

    def password_enter(self, password):
        self.send_the_keys(password, self._password_id)
        # self.get_password_file().send_keys(password)

    def click_login_button(self):
        self.click_element(self._button_login_xpath, locator_type="xpath")
        # self.get_button_login().click()

    def login(self, email_address="", password=""):
        self.click_login_link()
        self.clear_fields()
        self.email_enter(email_address)
        self.password_enter(password)
        time.sleep(2)
        self.click_login_button()

    def check_login_successful(self):
        result = self.check_elements_present("//*[@id='navbar']//span[text()='User Settings']",
                                             locator_type="xpath")
        return result, f"Login successful. Result: {result}."

    def check_login_failed(self):
        result = self.check_elements_present("//span[@class='dynamic-text help-block']",
                                             locator_type="xpath")
        return result

    def clear_fields(self):
        email_field = self.get_element(locator=self._addres_email_xpath, locator_type='xpath')
        email_field.clear()
        password_field = self.get_element(locator=self._password_id)
        password_field.clear()

