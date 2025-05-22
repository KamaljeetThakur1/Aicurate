from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def invalid_date_filter(url, invalid_start_date, invalid_end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "date_filter"))
        ).click()
        driver.find_element(By.ID, "start_date").send_keys(invalid_start_date)
        driver.find_element(By.ID, "end_date").send_keys(invalid_end_date)
        driver.find_element(By.ID, 'apply_filters').click()
        # Check for error messages
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Invalid date')]"))
        ).is_displayed(), "Error message not displayed for invalid dates." 
        print("Error message displayed for invalid date inputs.")
    except Exception as e:
        print(f"Filtering failed: {e}")
    finally:
        driver.quit()
