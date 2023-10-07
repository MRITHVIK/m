import pytest
from selenium import webdriver


@pytest.mark.usefixtures('test_apple')
def test_google():
        driver = webdriver.Chrome()
        driver.get('https://www.google.com/')
@pytest.mark.p
def test_facebook():
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/')