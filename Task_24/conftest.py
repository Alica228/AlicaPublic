import pytest
from selenium import webdriver


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = 'C:\\projects\\AlicaPublic\\Task_24\\chromedriver.exe'
    chrome_options.add_argument('--kiosk')
    return chrome_options


@pytest.yield_fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
