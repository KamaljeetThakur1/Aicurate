
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
    driver.find_element(By.ID, "pro-number-input").send_keys('invalid-Pro!@#')
    driver.find_element(By.ID, "apply-pro-filter").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'no-results-message'))) # Awaiting no results message
    print("Error displayed due to invalid PRO number")
except:
    print("Failed to filter with invalid PRO number")
finally:
    driver.quit()