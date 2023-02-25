import pytest

from paths import Paths
from selenium import webdriver


@pytest.fixture(scope="function")
def chromedriver(request):
    driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
    driver.maximize_window()
    driver.implicitly_wait(4)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time teardown.")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--ostype", help="Type of operating system.")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def ostype(request):
    return request.config.getoption("--ostype")