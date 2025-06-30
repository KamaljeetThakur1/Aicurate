
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_empty_needs_submission():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/login")
        # Simulate login
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("password123")
        driver.find_element(By.ID, "login").click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Identify Needs").click()
        time.sleep(2)
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        assert "This field is required" in driver.page_source
    finally:
        driver.quit()
