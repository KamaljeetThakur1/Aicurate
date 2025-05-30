
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_identify_needs_invalid_info():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 try:
 driver.get("http://example.com/login")
 WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login"))).click()
 time.sleep(1)
 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identify_needs"))).click()
 # Input invalid info
 driver.find_element(By.ID, "customer_info").send_keys("@@@@")
 assert "Invalid input" in driver.page_source
 print("Received error message for invalid input.")
 finally:
 driver.quit()
