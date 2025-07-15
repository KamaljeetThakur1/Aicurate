
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def clear_filters(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        # Click clear filters
        driver.find_element(By.ID, "clear_filters").click()
        time.sleep(2)
        # Verify original data is displayed
        assert "Original unfiltered data content" in driver.page_source
        print("Filters cleared successfully, showing unfiltered results.")
    except Exception as e:
        print(f"Clearing filters failed due to: {e}")
    finally:
        driver.quit()
