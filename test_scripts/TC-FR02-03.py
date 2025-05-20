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
        driver.get("https://example.com/data-view")
        # Assume filters were previously applied
        driver.find_element(By.ID, "clear-filters").click()
        time.sleep(2)
        assert "All records" in driver.page_source, "Data records not reset to original state"
        print("Filters cleared successfully.")
    except Exception as e:
        print(f"Filter clear test failed: {e}")
    finally:
        driver.quit()
