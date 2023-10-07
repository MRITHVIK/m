import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver.chrome import ChromeDriverManager


@pytest.mark.usefixtures('test_apple')
def test_google():
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://www.google.com/')
@pytest.mark.p
def test_facebook():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://www.facebook.com/')