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

