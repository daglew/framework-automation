import pytest


class TestLogin:

    def test_login_valid(self, open_login_page):
        page = open_login_page
        page.login(email_address="kasia.basia_69@interia.com", password="KASIA.BASIA")

        result_2 = page.check_login_successful()
        assert result_2, f"Result_2: {result_2} is not True."

    def test_login_invalid(self, open_login_page):
        page = open_login_page
        page.login(email_address="kasia.basia_69@interia.com", password="pKASIA.BASIA")
        result = page.check_login_failed()
        assert result, f"Result: {result} is not True."


