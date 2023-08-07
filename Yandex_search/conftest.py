import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="session")
def browser():
    #driver = webdriver.Chrome(executable_path=".chromdriver")
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
