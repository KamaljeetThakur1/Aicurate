from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filter_empty_pro_number():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/data-view")
        driver.find_element(By.ID, "filter-button").click()
        time.sleep(1)
        driver.find_element(By.ID, "filter-criteria").select_by_visible_text('Contains')
        driver.find_element(By.ID, "apply-filter").click()
        time.sleep(2)
        error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'PRO Number cannot be empty')]")
        assert error_message.is_displayed(), "Error message for empty PRO Number not shown"
        print("Error displayed correctly for empty input.")
    except Exception as e:
        print(f"Filter empty pro number test failed: {e}")
    finally:
        driver.quit()
