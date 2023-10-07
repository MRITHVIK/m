import pytest
from selenium import webdriver

@pytest.fixture
def test_apple():
    driver = webdriver.Chrome()
    aa= driver.get('https://www.apple.com/in/')
    print("am apple")
    pass
