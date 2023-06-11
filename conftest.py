import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
from utilities import read_configuration


@pytest.fixture()
def setup_and_teardown(request):
    global driver
    browser = read_configuration.read_config("basic info","browser")
    if browser.__eq__("chrome"):
        driver= webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("provide a valid browser name ")

    driver.maximize_window()
    app_url = read_configuration.read_config("basic info","url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
