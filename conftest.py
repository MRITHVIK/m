import pytest
from selenium import webdriver

@pytest.fixture
def test_fixture1(request):
    calling_test_name = request.node.name
    if calling_test_name == 'test_google':
     print(f"hi am {calling_test_name}")
     driver = webdriver.Chrome()
     driver.get('https://www.google.com/')
    if calling_test_name == 'test_facebook':
     print(f"hi am {calling_test_name}")
     driver = webdriver.Chrome()
     driver.get('https://www.facebook.com/')
    if calling_test_name == 'test_apple':
     print(f"hi am {calling_test_name}")
     driver = webdriver.Chrome()
     driver.get('https://www.apple.com/in/')
