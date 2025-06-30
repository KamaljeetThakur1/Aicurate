
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_multiple_users_access():
    drivers = []
    try:
        for i in range(5):
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.get("http://example.com/customer_interaction")
            assert "Interaction Options" in driver.page_source
            drivers.append(driver)
        time.sleep(10)
    finally:
        for driver in drivers:
            driver.quit()
