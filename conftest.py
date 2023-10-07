import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture
def test_apple():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    aa= driver.get('https://www.apple.com/in/')
    print("am apple")
    pass
