import pytest

from pages.login_page import PageLogin


@pytest.fixture(scope="function")
def open_login_page(chromedriver):
    page = PageLogin(chromedriver)
    return page

