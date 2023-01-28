
from selenium.webdriver.common.by import By


class PageLogin:
    def __init__(self, driver):
        self.driver = driver

    # loc
    _login_xpath = "//a[@href='/login']"
    _addres_email_id = "email"
    _password_id = "password"
    _button_login_xpath = "//input[@value='Login']"

    def get_login(self):
        return self.driver.find_element(By.XPATH, self._login_xpath)

    def get_addres_email(self):
        return self.driver.find_element(By.ID, self._addres_email_id)

    def get_password_file(self):
        return self.driver.find_element(By.ID, self._password_id)

    def get_button_login(self):
        return self.driver.find_element(By.XPATH, self._button_login_xpath)

    def click_login_link(self):
        self.get_login().click()

    def email_enter(self, email):
        self.get_login().send_keys(email)

    def password_enter(self, password):
        self.get_password_file().send_keys(password)

    def click_login_button(self):
        self.get_button_login().click()

    def login(self, email_address, password):
        self.click_login_link()
        self.email_enter(email_address)
        self.password_enter(password)
        self.click_login_button()

