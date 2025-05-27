
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://yourapp.com/data')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "filter-pro-number"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Contains']"))).click()
    driver.find_element(By.ID, "pro-number-input").send_keys('12345')
    driver.find_element(By.ID, "apply-pro-filter").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'filtered-results'))) # Awaiting filtered results 
    print("Results filtered successfully by PRO Number")
except:
    print("Failed to filter by PRO Number")
finally:
    driver.quit()