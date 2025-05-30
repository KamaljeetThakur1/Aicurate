
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_customer_interaction_no_login():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://example.com/customer_interaction")
 time.sleep(2)
 # Expected Result: Should be redirected to the login page
 assert "Login" in driver.title
 print("Redirected to login page as expected.")
 finally:
 driver.quit()
