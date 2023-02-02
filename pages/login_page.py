from selenium.webdriver.common.by import By
from base.selenium_driver_helpers import SeleniumDriverHelpers


class PageLogin(SeleniumDriverHelpers):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # loc
    _login_xpath = "//a[@href='/login']"
    _addres_email_xpath = "//input[@id='email'][@class='form-control input-md']"
    _password_id = "password"
    _button_login_xpath = "//input[@value='Login']"

    # def get_login(self):
    #     return self.driver.find_element(By.XPATH, self._login_xpath)
    #
    # def get_addres_email(self):
    #     return self.driver.find_element(By.XPATH, self._addres_email_xpath)
    #
    # def get_password_file(self):
    #     return self.driver.find_element(By.ID, self._password_id)
    #
    # def get_button_login(self):
    #     return self.driver.find_element(By.XPATH, self._button_login_xpath)

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

    def login(self, email_address, password):
        self.click_login_link()
        self.email_enter(email_address)
        self.password_enter(password)
        self.click_login_button()

