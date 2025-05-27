
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "clear-filters-btn"))).click()
    # Add an assertion to verify that filters have been cleared
    start_date = driver.find_element(By.ID, "start-date-picker").get_attribute('value')
    end_date = driver.find_element(By.ID, "end-date-picker").get_attribute('value')
    assert start_date == '' and end_date == ''
    print("Filters cleared successfully")
except:
    print("Failed to clear filters")
finally:
    driver.quit()