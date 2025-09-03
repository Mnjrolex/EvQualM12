import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Fixture to set up the browser
@pytest.fixture(scope="function")
def setup_browser():
    options = Options()
    options.add_argument("--headless")  # Running in headless mode (no GUI)
    driver = webdriver.Chrome(service=Service("path_to_chromedriver"), options=options)
    yield driver
    driver.quit()

# Smoke test (positive case)
@pytest.mark.smoke
@pytest.mark.positive
def test_title(setup_browser):
    driver = setup_browser
    driver.get("https://www.example.com")
    assert driver.title == "Example Domain"

# Negative test case
@pytest.mark.negative
def test_invalid_url(setup_browser):
    driver = setup_browser
    driver.get("https://www.nonexistentwebsite.com")
    assert "404" in driver.title

# Positive test case
@pytest.mark.positive
def test_element_existence(setup_browser):
    driver = setup_browser
    driver.get("https://www.example.com")
    element = driver.find_element(By.XPATH, "//h1")
    assert element.is_displayed()
