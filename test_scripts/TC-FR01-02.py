
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_interaction_page_invalid_url():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://example.com/invalid")
 time.sleep(2)
 # Expected Result: Error message should be displayed
 assert "404 Not Found" in driver.page_source
 print("Received error message for invalid URL.")
 finally:
 driver.quit()
