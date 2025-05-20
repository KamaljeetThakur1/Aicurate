from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def data_filter_invalid_dates(start_date, end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/data-view")
        driver.find_element(By.ID, "start-date").click()
        time.sleep(1)
        driver.find_element(By.ID, "start-date-input").send_keys(start_date)
        driver.find_element(By.ID, "end-date").click()
        time.sleep(1)
        driver.find_element(By.ID, "end-date-input").send_keys(end_date)
        driver.find_element(By.ID, "apply-filters").click()
        time.sleep(2)
        error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'End date must be after start date')]")
        assert error_message.is_displayed(), "Error message for invalid dates not shown"
        print("Invalid date error displayed correctly.")
    except Exception as e:
        print(f"Filter validation failed: {e}")
    finally:
        driver.quit()
