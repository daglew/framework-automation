import unittest
from selenium import webdriver
from paths import Paths


class InitializeWebDriver(unittest.TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
        self.driver.maximize_window()
        self.page = "https://letskodeit.teachable.com/"
        self.driver.implicitly_wait(4)
        self.driver.get(self.page)

    def tearDown(self):
        self.driver.close()


