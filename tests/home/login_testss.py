import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from paths import Paths


class LoginTests:
    def __init__(self):
        self.page = "https://courses.letskodeit.com"
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.get(self.page)
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)

    def test_login_valid(self):
        login = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        login.click()

        aaddres_email = self.driver.find_element(By.ID, "email")
        aaddres_email.clear()
        aaddres_email.send_keys("test@email.com")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("abcabc")
        time.sleep(4)

        button_login = self.driver.find_element(By.XPATH, "//input[@value='Login']")
        button_login.click()
        time.sleep(4)

        icon_user = self.driver.find_element(By.XPATH, ".//*[@id='navbar']//span[text()='User Settings']")
        if icon_user is not None:
            print("You have successfully logged in.")
        else:
            print("Failed to login successfully.")
        time.sleep(6)

        self.driver.close()


run_logintests = LoginTests()
run_logintests.test_login_valid()

