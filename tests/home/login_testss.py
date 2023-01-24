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

        email = self.driver.find_element(By.ID, "email")
        email.send_keys("test@email.com")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("abcabc")







        self.driver.close()





