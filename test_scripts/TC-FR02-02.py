
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://yourapp.com/data-filter')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "start-date-picker"))).send_keys('2023-02-01')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "end-date-picker"))).send_keys('2023-01-31')
    driver.find_element(By.ID, "apply-filters-btn").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "error-message")))
    print("Error message displayed for invalid date range")
except:
    print("No error occurred when it should have")
finally:
    driver.quit()