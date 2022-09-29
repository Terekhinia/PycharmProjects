import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome('../pythonProject/chromedriver.exe')
    yield driver
    driver.quit()

