
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
        driver.get('https://example.com/data')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "startDate"))).send_keys('2023-01-01')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "endDate"))).send_keys('2023-01-31')
        driver.find_element(By.ID, "clearFilters").click()
        assert driver.find_element(By.ID, "startDate").text == ''
        assert driver.find_element(By.ID, "endDate").text == ''
        print("Filters cleared successfully.")
    except Exception as e:
        print(f"Clear failed: {e}")
    finally:
        driver.quit()
clear_filters()
