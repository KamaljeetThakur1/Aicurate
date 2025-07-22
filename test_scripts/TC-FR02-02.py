
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filter_data_invalid_dates():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://application-url/data-filter")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "startDatePicker"))).click()
        driver.find_element(By.XPATH, "//td[@data-date='2023-01-01']").click()
        driver.find_element(By.ID, "endDatePicker").click()
        driver.find_element(By.XPATH, "//td[@data-date='2023-01-01']").click()
        driver.find_element(By.ID, 'applyFilters').click()
        error_message = driver.find_element(By.XPATH, "//div[@class='error']").text
        assert error_message == "End date must be after start date."
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
