from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def clear_filters():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/data-filter")
        driver.find_element(By.ID, "startDate").send_keys("2023-01-01")
        driver.find_element(By.ID, "endDate").send_keys("2023-12-31")
        driver.find_element(By.XPATH, "//button[@id='filterButton']").click()
        time.sleep(2)
        driver.find_element(By.ID, "clearFiltersButton").click()
        time.sleep(2)
        assert "Default data displayed" in driver.page_source
        print("Filters cleared successfully.")
    except Exception as e:
        print(f"Clearing filters failed: {e}")
    finally:
        driver.quit()
clear_filters()