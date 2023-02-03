import time
from selenium import webdriver
from pages.login_page import PageLogin
from paths import Paths
import unittest


class LoginTests:
    def __init__(self):
        self.page = "https://courses.letskodeit.com"
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.get(self.page)
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)

    def test_login_valid(self):
        log_page = PageLogin(self.driver)
        log_page.login(email_address="test@email.com", password="abcabc")

        # icon_user = self.driver.find_element(By.XPATH, "//*[@id='navbar']//span[text()='User Settings']")
        # if icon_user is not None:
        #     print("You have successfully logged in.")
        # else:
        #     print("Failed to login successfully.")
        time.sleep(4)
        self.driver.close()


run_logintests = LoginTests()
run_logintests.test_login_valid()

