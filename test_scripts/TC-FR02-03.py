from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def clear_filter(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "date_filter"))
        ).click()
        driver.find_element(By.ID, "start_date").send_keys('2022-01-01')  # Sample valid date
        driver.find_element(By.ID, "end_date").send_keys('2022-12-31')  # Sample valid date
        driver.find_element(By.ID, 'apply_filters').click()  # Apply filters
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "clear_filters"))
        ).click()  # Click Clear Filters
        # Verify if all data is visible again (Assume a predefined method check_all_data_visible)
        assert check_all_data_visible(driver), "Not all data is displayed after clearing filters." 
        print("Filters cleared successfully and all data is visible.")
    except Exception as e:
        print(f"Clearing filters failed: {e}")
    finally:
        driver.quit()
