import pytest

from base.factory_web_driver import FactoryWebDriver
from paths import Paths
from selenium import webdriver


@pytest.fixture()
def setup():
    print("Running method level setup.")
    yield
    print("Running method level teardown.")


@pytest.fixture(scope="class")
def one_time_setup(request, browser):
    print("Running one_time_setup.")
    fwd = FactoryWebDriver(browser)
    driver = fwd.get_instance_web_driver()
    # if browser == "firefox":
    #     page = "https://courses.letskodeit.com"
    #     driver = webdriver.Chrome(executable_path=Paths.CHROMEDRIVER_PATH)
    #     driver.maximize_window()
    #     driver.implicitly_wait(4)
    #     driver.get(page)
    #     print("Running tests on FF.")
    # else:
    #     page = "https://courses.letskodeit.com"
    #     driver = webdriver.Chrome()
    #     driver.get(page)
    print("Running tests on chrome.")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time teardown.")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--ostype", help="Type of operating system.")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def ostype(request):
    return request.config.getoption("--ostype")



