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
        driver.get("http://example.com/data")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "proFilterMenu"))).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//option[text()='Contains']").click()
        time.sleep(1)
        driver.find_element(By.ID, "proNumberInput").send_keys("12345")
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "applyProFilter"))).click()
        time.sleep(2)
        filtered_data = driver.find_element(By.XPATH, "//div[@class='data-display']").is_displayed()
        assert filtered_data == True
        print("Data filtered by PRO Number successfully.")
    except Exception as e:
        print(f"Filtering by PRO Number failed: {e}")
    finally:
        driver.quit()
