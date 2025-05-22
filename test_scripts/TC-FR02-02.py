from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filter_data_invalid_date():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/data-filter")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='filterButton']"))
        )
        driver.find_element(By.ID, "startDate").send_keys("2023-12-31")
        driver.find_element(By.ID, "endDate").send_keys("2023-01-01")
        driver.find_element(By.XPATH, "//button[@id='filterButton']").click()
        time.sleep(2)
        assert "Invalid date range" in driver.page_source
        print("Error message is displayed for invalid date range.")
    except Exception as e:
        print(f"Filter failed: {e}")
    finally:
        driver.quit()
filter_data_invalid_date()