from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class SeleniumDriverHelpers:
    def __init__(self, driver):
        self.driver = driver

    def get_element_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "linktext":
            return By.LINK_TEXT
        else:
            print(f"The given locator is invalid: {locator_type}.")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_element_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            print("The specified item was found.")
        except:
            print("The specified item was not found.")
        return element

    def click_element(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            print(f"An item with was clicked a locator: {locator} and locator_type: {locator_type}.")
        except:
            print(f"Cannot be clicked element with locator: {locator} and locator_type: {locator_type}.")
            print_stack()

    def present_element(self, locator, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            by_type = self.get_element_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            if element is not None:
                print("The specified item was found.")
                return True
            else:
                return False
        except:
            print("The specified item was not found.")
            return False

    def check_elements_present(self, locator, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            by_type = self.get_element_type(locator_type)
            list_elements = self.driver.find_elements(by_type, locator)
            if len(list_elements) > 0:
                print("The specified item was found.")
                return True
            else:
                print("The specified item was not found.")
                return False
        except:
            print("The specified item was not found.")
            return False

    def for_element_wait(self, locator, type_locator="id", timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type_element = self.get_element_type(locator_type=type_locator)

            print(f"Waiting for a maximum of: {str(timeout)} seconds for element to be visible.")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((by_type_element, locator)))
            print(f"Element appeared on the page.")
        except:
            print(f"Element not appeared on the page.")
            print_stack()
        return element




