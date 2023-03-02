import time
import traceback
import logging
import random
import string
import utilities.custom_logger as cust_log


class Util(object):
    log = cust_log.custom_logger(log_level=logging.INFO)

    def sleep(self, sec, info=""):
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "'seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def get_numeric_alpha(self, length, type='letters'):
        alphanumeric = ''
        if type =='lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alphanumeric.join(random.choice(case) for i in range(length))

    def get_name_unique(self, char_count=10):
        return self.get_numeric_alpha(length=char_count, type='lower')

    def get_list_unique_names(self, size_list=5, length_item=None):
        list_name = []
        for i in range (0, size_list):
            list_name.append(self.get_name_unique(length_item[i]))
            return list_name

    def check_text_contains(self, actual_text, expected_text):
        self.log.info("The actual text from the application's web interface --> :: " + actual_text)
        self.log.info("The expected text from the application's web interface --> :: " + expected_text)
        if expected_text.lower() in actual_text.lower():
            self.log.info("### INCLUDE VERIFICATION !!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT INCLUDE !!")
            return False

    def include_verify_text(self, actual_text, expected_text):
        self.log.info("The actual text from the application's web interface --> :: " + actual_text)
        self.log.info("The expected text from the application's web interface --> :: " + expected_text)
        if actual_text.lower() == expected_text.lower():
            self.log.info("### INCLUDE VERIFICATION !!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT INCLUDE !!")
            return False

    def check_list_match(self, actual_list, expected_list):
        return set(expected_list) == set(actual_list)

    def check_list_compatibility(self, actual_list, expected_list):
        lenght = len(expected_list)
        for i in range(0, lenght):
            if expected_list[i] not in actual_list:
                return False
        else:
            return True

