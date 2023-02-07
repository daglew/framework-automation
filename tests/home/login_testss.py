import pytest
from pages.login_page import PageLogin
import unittest


@pytest.mark.usefixtures("one_time_setup", "setup")
class LoginTests(unittest.TestCase):

    @pytest.fixture()
    def classSetup(self, one_time_setup):
        self.log_page = PageLogin(self.driver)

    def test_login_valid(self):
        self.log_page.login(email_address="kasia.basia_69@interia.com", password="KASIA.BASIA")
        result = self.log_page.check_login_successful()
        assert result, f"Result: {result} is not True."
        # time.sleep(4)
        # self.driver.quit()

    def test_login_invalid(self):
        # self.driver.get(self.page)
        self.log_page.login(email_address="kasia.basia_69@interia.com", password="pKASIA.BASIA")
        result = self.log_page.check_login_failed()
        assert result, f"Result: {result} is not True"
        # time.sleep(4)
        #
        # self.driver.close()
