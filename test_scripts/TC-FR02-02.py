
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def filter_data_invalid_date():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get('https://example.com/data')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "startDate"))).send_keys('2023-01-31')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "endDate"))).send_keys('2023-01-01')
        driver.find_element(By.ID, "applyFilters").click()
        error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "error")))
        assert 'End date must be after start date' in error_message.text
        print("Error message displayed correctly for invalid date range.")
    except Exception as e:
        print(f"Filtering failed: {e}")
    finally:
        driver.quit()
filter_data_invalid_date()
