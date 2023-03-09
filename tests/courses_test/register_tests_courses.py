from base.page_base import PageBase
import logging
import utilities.custom_logger as cust_log


class RegisterTestsCourses(PageBase):
    log = cust_log.custom_logger(log_level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.page = self.driver.get("https://courses.letskodeit.com")



"""
Locators
"""
sign_in_button_id = "navbar-inverse-collapse"
password_button_id = "password"
login_button_id = "login"
all_courses_click = "ALL COURSES"
course = "//a[@href='/courses/{0}']"
enroll_button_link_text = "ENROLL NOW"
card_number_xpath = "//input[@name='cardnumber']"
expiry_date_id = "card-expiry"
security_code_id = "card-cvc"
enroll_message_error = "//div[@class='card-errors has-error']"


    def course_name(self, name):
        self.

    def course_to_enroll_select(self, full_course_name):
        print()

