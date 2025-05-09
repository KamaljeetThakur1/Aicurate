from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def filter_invalid_pro_number(url, invalid_pro_number):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        # Open filter menu
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "filterDropdown"))
        ).click()
        # Select 'Contains'
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//option[text()='Contains']"))
        ).click()
        # Enter invalid PRO Number
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "proNumberInput"))
        )
        input_field.send_keys(invalid_pro_number)
        # Click apply filter
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Apply Filter']"))
        ).click()
        # Expect validation error
        assert "No results found" in driver.page_source
    except Exception as e:
        print(f"Failed to filter by invalid PRO Number: {e}")
    finally:
        driver.quit()
