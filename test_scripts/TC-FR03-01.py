
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
        driver.get('https://example.com/dataset')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "filterButton"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "criteria"))).select_by_visible_text('Contains')
        driver.find_element(By.ID, "proNumberInput").send_keys('PRO12345')
        driver.find_element(By.ID, "applyFilter").click()
        results = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "resultEntry")))
        assert len(results) > 0
        print("Dataset filtered successfully by PRO Number.")
    except Exception as e:
        print(f"Filtering failed: {e}")
    finally:
        driver.quit()
filter_by_pro_number()
