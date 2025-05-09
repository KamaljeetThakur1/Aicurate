from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def apply_date_filter(url, start_date, end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        # Select start date
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "startDatePicker"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@aria-label='{start_date}']"))
        ).click()
        # Select end date
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "endDatePicker"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@aria-label='{end_date}']"))
        ).click()
        # Apply filters
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Apply Filters']"))
        ).click()
        # Verify data is filtered
        assert "Filtered results" in driver.page_source
        print("Date filter applied successfully.")
    except Exception as e:
        print(f"Failed to apply date filter: {e}")
    finally:
        driver.quit()
