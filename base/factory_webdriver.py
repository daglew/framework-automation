import traceback
from selenium import webdriver
from paths import Paths
from base.initialize_webdriver import InitializeWebDriver


class FactoryWebDriver:
    def __init__(self, browser):
        self.browser = browser
        self.driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)

    def get_instance_web_driver(self):
        page = "https://courses.letskodeit.com"
        if self.browser == "firefox":
            self.driver = webdriver.Firefox()
        elif self.browser == "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)
        self.driver.get(page)
        return self.driver

