
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def clear_filters_after_apply():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("http://application-url/data-filter")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "applyFilters"))).click()
        driver.find_element(By.ID, 'clearFilters').click()
        all_records_displayed = driver.find_element(By.ID, "dataTable").is_displayed()
        assert all_records_displayed
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()
