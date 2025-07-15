
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def filter_data_by_date(url, start_date, end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        # Navigate to filter section
        driver.find_element(By.ID, "filter_section").click()
        # Select start date
        driver.find_element(By.ID, "start_date_picker").send_keys(start_date)
        # Select end date
        driver.find_element(By.ID, "end_date_picker").send_keys(end_date)
        # Click apply filter
        driver.find_element(By.ID, "apply_filter").click()
        time.sleep(2)
        # Verify results updated
        assert "data filtered" in driver.page_source
        print("Data filtered successfully between the selected dates.")
    except Exception as e:
        print(f"Filtering failed due to: {e}")
    finally:
        driver.quit()
