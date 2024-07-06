import os.path
import os
from datetime import datetime

import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        print("****chrome launched****")
        return driver

    elif browser == 'edge':
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
        print("****Edge launched****")
        return driver

    elif browser == 'firefox':
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        print("****Firefox launched****")
        return driver

    else:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        print("****chrome launched****")
        return driver


def pytest_addoption(parser):  # this will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # this will return the browser value to set up method
    return request.config.getoption("--browser")


###########Pytest fixture for HTML Reports ############

def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Sai'

#Specifying report folder location and save report with timestamp

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    timestamp = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    folder_path = r"C:\Users\yalam\PycharmProjects\opecartv1\Opencart\reports"
    config.option.htmlpath = os.path.join(folder_path, timestamp +".html")


#It is hook for adding Environment info into the html report

# @pytest.mark.optionalhook
# def pytest_metedata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("plugins", None)












# Below is the breakdown explanation of this fixture

# @pytest.fixture():

#This decorator marks the setup function as a pytest fixture,
#which will be used to set up WebDriver instances for tests.


# Service Initialization:

# service = Service(ChromeDriverManager().install()): This line initializes the ChromeDriver service
# using ChromeDriverManager().install().

# ChromeDriverManager().install() downloads the latest version of ChromeDriver
# if not already installed and returns the path to it.


# WebDriver Initialization:

# driver = webdriver.Chrome(service=service): Here, you create a Chrome WebDriver instance
# and pass the service object as an argument. This connects the WebDriver instance
# to the ChromeDriver service you previously configured.

# Return Statement:

# return driver: This returns the initialized WebDriver instance (driver)
# to any test function that uses this fixture.
