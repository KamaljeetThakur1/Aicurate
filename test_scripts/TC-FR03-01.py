from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filter_by_pro_number(pro_number):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/data-view")
        driver.find_element(By.ID, "filter-button").click()
        time.sleep(1)
        driver.find_element(By.ID, "filter-criteria").select_by_visible_text('Contains')
        driver.find_element(By.ID, "pro-number-input").send_keys(pro_number)
        driver.find_element(By.ID, "apply-filter").click()
        time.sleep(2)
        assert "Filtered results" in driver.page_source, "Pro number filtering failed"
        print("Data filtered correctly by PRO Number.")
    except Exception as e:
        print(f"Filter test failed: {e}")
    finally:
        driver.quit()
