from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def apply_invalid_date_filter(url, invalid_start_date, invalid_end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        # Select invalid start date
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "startDatePicker"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@aria-label='{invalid_start_date}']"))
        ).click()
        # Select end date
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "endDatePicker"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@aria-label='{invalid_end_date}']"))
        ).click()
        # Try applying filters
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Apply Filters']"))
        ).click()
        # Expect validation error
        assert "Invalid date selected" in driver.page_source
        print("Validation error for invalid dates triggered successfully.")
    except Exception as e:
        print(f"Failed to apply invalid date filter: {e}")
    finally:
        driver.quit()
