import pytest
from datetime import datetime
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#### Pytest HTML Report ####

# It is hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'Customer Registration'
    config._metadata['Tester'] = 'Chetan Mirajkar'


# It is hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)


# Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\" + datetime.now().strftime(
        "%d-%m-%Y %H-%M-%S") + ".html"
