from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def clear_filters(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(url)
        # Click clear filters
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Clear Filters']"))
        ).click()
        # Verify filters are cleared
        assert "Default data state displayed" in driver.page_source
        print("Filters cleared successfully.")
    except Exception as e:
        print(f"Failed to clear filters: {e}")
    finally:
        driver.quit()
