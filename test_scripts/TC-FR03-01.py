from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filter_by_pro_number():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://example.com/dataset")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "filterMenuButton"))
        ).click()
        driver.find_element(By.XPATH, "//option[contains(text(), 'Contains')]").click()
        driver.find_element(By.ID, "proNumberInput").send_keys("PRO12345")
        driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]").click()
        time.sleep(2)
        assert "PRO12345" in driver.page_source
        print("Dataset updates successfully with PRO number filter.")
    except Exception as e:
        print(f"Filter failed: {e}")
    finally:
        driver.quit()
filter_by_pro_number()