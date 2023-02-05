import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

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
        self.log_page = PageLogin(self.driver)

    @pytest.mark.run(order=2)
    def test_login_valid(self):
        self.driver.get(self.page)
        self.log_page.login(email_address="kasia.basia_69@interia.com", password="KASIA.BASIA")
        result = self.log_page.check_login_successful()
        assert result, f"Result: {result} is not True."

        time.sleep(4)
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_login_invalid(self):
        self.driver.get(self.page)
        self.log_page.login(email_address="kasia.basia_69@interia.com", password="pKASIA.BASIA")
        result = self.log_page.check_login_failed()
        assert result, f"Result: {result} is not True"
        time.sleep(4)

        self.driver.close()


run_logintests = LoginTests()
run_logintests.test_login_valid()
run_logintests.test_login_invalid()
