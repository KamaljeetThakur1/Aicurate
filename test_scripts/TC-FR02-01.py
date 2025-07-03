
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def filter_data_by_date():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('https://example.com/data')
        assert 'Data' in driver.title
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "startDate"))).send_keys('2023-01-01')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "endDate"))).send_keys('2023-01-31')
        driver.find_element(By.ID, "applyFilters").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "filteredResults")))
        print("Data filtered successfully.")
    except Exception as e:
        print(f"Filtering failed: {e}")
    finally:
        driver.quit()
filter_data_by_date()
