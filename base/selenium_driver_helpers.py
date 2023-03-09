import time
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging
import utilities.custom_logger as cust_log
import os


class SeleniumDriverHelpers:
    log = cust_log.custom_logger(log_level=logging.DEBUG)[0]

    def __init__(self, driver):
        self.driver = driver

    def screen_shot(self, result_message):
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        directory_screenshot = "../screenshots/"
        file_name_relative = directory_screenshot + file_name
        directory_current = os.path.dirname(__file__)
        file_destination = os.path.join(directory_current, file_name_relative)
        directory_destination = os.path.join(directory_current, directory_screenshot)

        try:
            if not os.path.exists(directory_destination):
                os.makedirs(directory_destination)
            self.driver.screenshot_save(file_destination)
            self.log.info(f"Save the screenshot in the directory: {file_destination}")
        except:
            self.log.error("### Exception occurred.")
            print_stack()

    def get_title(self):
        return self.driver.title

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
            self.log.info(f"The given locator is invalid: {locator_type}.")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_element_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("The specified item was found.")
        except:
            self.log.info("The specified item was not found.")
        return element

    def send_the_keys(self, data, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info(f"Sent data on element with locator: : {locator} and locator_type: {locator_type}.")
        except:
            self.log.info(f"Cannot send data on the element with locator: {locator} and locator_type: {locator_type}.")
            print_stack()

    def get_element_list(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            type_by = self.get_element_type(locator_type)
            element = self.driver.find_element(type_by, locator)
            self.log.info("Found element list of items with locator: " + locator + "and locator_type: " + locator_type)
        except:
            self.log.info("List of element not found using locator: " + locator + "and locator_type: " + locator_type)
        return element

    def click_element(self, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info(f"An item with was clicked a locator: {locator} and locator_type: {locator_type}.")
        except:
            self.log.info(f"Cannot be clicked element with locator: {locator} and locator_type: {locator_type}.")
            print_stack()

    def present_element(self, locator, locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("The specified item was found locator: " + locator + "locator_type: " + locator_type)
                return True
            else:
                self.log.info("There is no item in the locator: " + locator + "locator_type: " + locator_type)
                return False
        except:
            self.log.info("The specified item was not found.")
            return False

    def check_elements_present(self, locator, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            by_type = self.get_element_type(locator_type)
            list_elements = self.driver.find_elements(by_type, locator)
            if len(list_elements) > 0:
                self.log.info("The specified item was found locator: " + locator + "locator_type: " + locator_type)
                return True
            else:
                self.log.info("The specified item was not found: " + locator + "locator_type: " + locator_type)
                return False
        except:
            self.log.info("The specified item was not found.")
            return False

    def for_element_wait(self, locator, locator_type="id", timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type_element = self.get_element_type(locator_type=locator_type)

            self.log.info(f"Waiting for a maximum of: {str(timeout)} seconds for element to be visible.")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((by_type_element, locator)))
            self.log.info(f"Element appeared on the page.")
        except:
            self.log.infogetheader(f"Element not appeared on the page.")
            print_stack()
        return element

    def text_get(self, locator="", locator_type="id", element=None, info=""):
        try:
            if locator:
                self.log.debug("locator in condition.")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding the text.")
            text = element.text
            self.log.debug("Once the item is found, the size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("getting text on element :: " + info)
                self.log.info("text is ::'" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def displayed_is_element(self, locator="", locator_type="id", element=None):
        displayed = False
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                displayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locator_type: " + locator_type)
            else:
                self.log.info("Element is  not displayed with locator: " + locator + " locator_type: " + locator_type)
            return displayed
        except:
            print("Element not found")
            return False

    def scroll_web(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scroll_by(0, -1000);")
        if direction == "down":
            self.driver.execute_script("window.scroll_by(0, 1000);")

