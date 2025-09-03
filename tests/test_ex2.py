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

# Negative test case for element not found
@pytest.mark.negative
def test_element_not_found(setup_browser):
    driver = setup_browser
    driver.get("https://www.example.com")
    try:
        driver.find_element(By.XPATH, "//nonexistent-element")
        assert False, "Element should not exist."
    except:
        assert True  # Pass if element is not found

# Positive test case: Checking the button text
@pytest.mark.positive
def test_button_text(setup_browser):
    driver = setup_browser
    driver.get("https://www.example.com")
    button = driver.find_element(By.XPATH, "//a[@href='http://www.iana.org/domains/example']")
    assert button.text == "More information..."
