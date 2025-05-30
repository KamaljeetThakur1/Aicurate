
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_customer_interaction():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://example.com/login")
 WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login"))).click()
 time.sleep(1)
 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "customer_interaction"))).click()
 # Expected Result: Customer interaction page is displayed
 assert "Customer Interaction" in driver.title
 print("Customer interaction page displayed successfully.")
 finally:
 driver.quit()
