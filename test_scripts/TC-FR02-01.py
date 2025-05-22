from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def date_filter(url, start_date, end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "date_filter"))
        ).click() # Open date filter
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "start_date"))).send_keys(start_date)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "end_date"))).send_keys(end_date)
        driver.find_element(By.ID, 'apply_filters').click() # Click on Apply Filters
        # Verify if data is filtered correctly (Assume a predefined method check_data_range)
        assert check_data_range(driver, start_date, end_date), "Data not filtered as expected." 
        print("Data filtered successfully.")
    except Exception as e:
        print(f"Filtering failed: {e}")
    finally:
        driver.quit()
