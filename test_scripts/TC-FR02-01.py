
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "start-date-picker"))).send_keys('2023-01-01')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "end-date-picker"))).send_keys('2023-01-31')
    driver.find_element(By.ID, "apply-filters-btn").click()
    # Add an assertion to check if filtered data is displayed
    filtered_data = driver.find_element(By.CLASS_NAME, 'filtered-results')
    assert filtered_data.is_displayed()
    print("Data filtered successfully for the selected date range")
except:
    print("Failed to apply date filters")
finally:
    driver.quit()