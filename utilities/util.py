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


