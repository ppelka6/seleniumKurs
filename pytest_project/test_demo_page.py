import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def test_setup():
    # op = Options()
    # op.add_experimental_option("detach", True)
    # op.add_argument("--disable-dev-shm-usage")
    # op.add_argument("--disable-gpu")
    # op.add_argument("--no-sandbox")
    global driver
    driver: WebDriver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=op)
    driver.get("C:/Users/48730/Downloads/Test.html")
    driver.maximize_window()
    yield
    driver.quit()


def test_method(test_setup):
    assert driver.title == "Strona testowa"