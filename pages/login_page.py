import time

from selenium.webdriver.common.by import By


class PageLogin:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email_address, password_):
        login = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        login.click()

        aaddres_email = self.driver.find_element(By.ID, "email")
        aaddres_email.clear()
        aaddres_email.send_keys(email_address)

        password = self.driver.find_element(By.ID, "password")
        password.send_keys(password_)
        time.sleep(4)

        button_login = self.driver.find_element(By.XPATH, "//input[@value='Login']")
        button_login.click()

