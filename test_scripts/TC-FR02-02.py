from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def apply_invalid_date_filters():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://example.com/data")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "startDatePicker"))).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//td[@data-date='2023-01-31']").click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "endDatePicker"))).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//td[@data-date='2023-01-01']").click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "applyFilters"))).click()
        time.sleep(2)
        error_message = driver.find_element(By.XPATH, "//div[@class='validation-error']").is_displayed()
        assert error_message == True
        print("Validation error displayed for invalid date selection.")
    except Exception as e:
        print(f"Filtering failed: {e}")
    finally:
        driver.quit()
