# test_launch_browsers.py

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# This fixture will start the Chrome driver for each test
@pytest.fixture
def driver():
    # Set up Chrome WebDriver
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Update with your path
    driver.maximize_window()
    yield driver
    driver.quit()

# Test to launch YouTube
def test_launch_youtube(driver):
    driver.get('https://www.youtube.com')
    
    # Wait for the page to load (simple implicit wait)
    time.sleep(3)
    
    # Verify the page title contains 'YouTube'
    assert 'YouTube' in driver.title
    
    # You can also verify the page by checking if a certain element exists
    assert driver.find_element(By.XPATH, '//input[@id="search"]')  # Check if the search box exists

# Test to launch Amazon
def test_launch_amazon(driver):
    driver.get('https://www.amazon.com')
    
    # Wait for the page to load (simple implicit wait)
    time.sleep(3)
    
    # Verify the page title contains 'Amazon'
    assert 'Amazon' in driver.title
    
    # Check if the search bar is present
    assert driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]')  # Amazon search bar
